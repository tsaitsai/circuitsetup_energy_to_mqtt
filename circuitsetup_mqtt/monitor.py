##########################################################################
# Much of this code was copied from Margaret Johnson's (@BitKnitting)
# FHmonitor project https://github.com/BitKnitting/FHmonitor
# 
# 2020-09:  Eric Tsai
#           parameterize SPI groupings to read multiple CircuitSetup
#           monitoring boards and publish readings to MQTT
#           Not Done:  THD, phase angle, publish on minimum change
#########################################################################

'''

--start script
python3 monitor.py

--view logs
journalctl | tail

*** todo ***
1.  Set MQTT broker
2.  Append the right number of circuits
3.  Calibrate AC adapter gain and current transformer gain
4.  Set reading rate by changing sleep time


'''


from error_handling import handle_exception
from atm90_e32_pi import ATM90e32

import board
import digitalio
import logging
logger = logging.getLogger(__name__)
import paho.mqtt.client as mqtt
import time
from datetime import datetime

logging.basicConfig(level=logging.WARNING)

# Set to false if don't want regular readings, and want to send readings if > minimum change
ALWAYS_PUBLISH = True

class Monitor:
    """

    """
    def on_connect(client, userdata, flags, rc):
        print("Connected with result code "+str(rc))
        try:
            self.client.publish("/emon/heartbeat", "connected", qos=0)
        except:
            time.sleep(3)

    def on_disconnect(client, userdata,rc=0):
        print("disconnected with result code "+str(rc))
        self.client.reconnect
    
    def __init__(self, led_pin=None):
        #logger.setLevel(logging.warning)
        self.debug = False
        #if using ctrl_c or restarting a lot, set this to False.  If run in background, set to True
        self.as_service = True

        self.db = None
        self.t_heartbeat = time.perf_counter()
        
        self.circuit = []
        self.num_circuit = 0
        
        self.energy_sensor = None
        self.energy_sensor2 = None
        self.energy_sensor3 = None
        self.energy_sensor4 = None
        if led_pin is None:
            led_pin = board.D18  # We always wire to GPIO 18.
        self.led = digitalio.DigitalInOut(board.D18)
        self.led.direction = digitalio.Direction.OUTPUT
        
        self.client = mqtt.Client()
        self.client.on_disconnect = self.on_disconnect

        logging.warning('started emon..')
        try:
            # *** todo ***
            self.client.connect("192.168.1.115",1883,60)
            if self.as_service:
                logging.warning('emon start in threaded mqtt mode')
                try:
                    self.client.loop_start()
                except:
                    logging.warning('emon fail to start loop')
        except:
            time.sleep(10)
        
    ####################################################
    # Initialize the energy sensor.  The properties are
    # are written to atm90e32 registers during initialization.
    # They are specific to the Power and Current Transformers
    # being used.  An exception occurs if the write cannot
    # be verified.
    ####################################################

    def init_sensor(self):
        """
        Initialize the atm90e32 by setting the calibration registry properties.
        """
        linefreq_60hz = 4485
        #pga gain = amps to house.  100amps = 21, >100amps = 42
        gain_pga_100amp = 21


        # *** todo ***
        # Replace values with the correct calibration values after performing calibration
        gain_voltage_ACA_01 = 7508    # AC adapter model 01, voltage gain for 1st module (circuits 0 and 1)
        gain_voltage_ACA_02 = 7261    # AC adapter model 02, voltage gain for 2nd module (circuits 2 and 3)

        # *** todo ***
        # current gain for different current transformers (20A, 80A, and 100A transformers)
        # if you buy identical 20A split core transformers, they can use the same current gain.  If you ebay it and 
        # use a bunch of different 20A current transformers, may need to calibrate individually ie "20A_00", "20A_01"
        gain_current_20A_00 = 5511      # emon_current / real current = x/gain_current, new_gain_current=5511
        gain_current_80A_00 = 20966     # emon_current / real current = x/gain_current, new_gain_current=20966
        gain_current_100A_00 = 13777    # emon_current / real current = x/gain_current, new_gain_current=13777
        
        try:

            #  Hardcode each circuit's calibration parameters based on AC adapter used and voltage transformer used.
            #  Using two 6-channel CircuitSetup modules, we actually have four circuits and 3 channels per circuit.
            #  Each circuit needs to be instantiated with a single AC adapter voltage gain and three 
            #    current transformer current gain (one per channel).
            #  ATM90e32(linefreq, gain_pga_100amp, AC_ADAPTER_voltage_gain, ...
            #           ch_0_xfmr_current_gain, ch_1_xfmr_current_gain, ch_2_xfmr_current_gain, raspberry_pi_cc_pin)
            #
            #
            # *** todo ***
            #First Module:  circuit 0, channel 0-2;  Phase A
            self.circuit.append(ATM90e32(linefreq_60hz, gain_pga_100amp, gain_voltage_ACA_01, gain_current_100A_00, gain_current_80A_00, gain_current_20A_00, board.D5))
            
            #First Module:  circuit 1, channel 0-2;  Phase A
            self.circuit.append(ATM90e32(linefreq_60hz, gain_pga_100amp, gain_voltage_ACA_01, gain_current_20A_00, gain_current_20A_00, gain_current_20A_00, board.D6))
            
            #Second Module:  circuit 2, channel 0-2;  Phase B
            self.circuit.append(ATM90e32(linefreq_60hz, gain_pga_100amp, gain_voltage_ACA_02, gain_current_100A_00, gain_current_20A_00, gain_current_20A_00, board.D13))
            
            #Second Module:  circuit 3, channel 0-2;  Phase B
            self.circuit.append(ATM90e32(linefreq_60hz, gain_pga_100amp, gain_voltage_ACA_02, gain_current_20A_00, gain_current_80A_00, gain_current_20A_00, board.D19))
            
            #append more circuits as needed, or delete as needed
            
            self.num_circuit = len(self.circuit)  # returns 4 for two 6-channel boards

            # generate unique mqtt topics based on circuit number and channel
            # circuit 0, channel 0
            # self.circuit[0].readings_ray[0]["name"] = "c0c0"
            # With two 6-channel circuit setup modules, we have 4 circuits with 3 channels each, like this:
            #   c0c0, c0c1, c0c2
            #   c1c0, c1c1, c1c2
            #   c2c0, c2c1, c2c2
            #   c3c0, c3c1, c3c2
            for i in range(len(self.circuit)):
                for j in range(len(self.circuit[i].readings_ray)):
                    # c0c1 = circuit 0, channel 1
                    # self.circuit[0].readings_ray[1]["name"] = "c0c1"
                    self.circuit[i].readings_ray[j]["name"] = "c" + str(i) + "c" + str(j)

            # Option to use minimum change to send updates
            # intialize sane min change values so we're not reporting too much
            # individual:  self.circuit[0].readings_min_change["line_current"] = .02
            for x in self.circuit:
                # means self.circuit[0, 1, 2, 3].get_all_readings()
                #newreadings = x.get_all_readings()
                #for y in range(len(x.readings_ray)):
                for y in x.readings_min_change:
                    # means x.readings_ray[0, 1, 2], y=0, 1, 2 objects
                    y["line_volt"] = 2.0
                    y["line_current"] = -1
                    y["power_active"] = -1
                    y["power_reactive"] = -1
                    y["power_apparent"] = -1
                    y["power_factor"] = 1000.0
                    y["phase_angle"] = 1
                    y["THD_volt"] = 1
                    y["THD_current"] = 1
                for z in range(len(x.update_interval)):
                    x.update_interval[z] = 25.0
                # todo:  add minimum time
                #for x.readings_min_time = 10 seconds

            #debug print
            #print("----- double check min values ----")
            for x in self.circuit:
                for y in x.readings_min_change:
                    # means x.readings_min_change[0, 1, 2], y=0, 1, 2 objects
                    for z in y:
                        #print(str(z), y[z])
                        pass


            logger.info('Energy meter has been initialized.')
            sys0 = self.circuit[0].sys_status0
            if (sys0 == 0xFFFF or sys0 == 0):
                e = 'EXCEPTION: Cannot connect to the energy meter.'
                handle_exception(e)
            logger.info('Energy meter is working.')
            return True
        except Exception as e:
            handle_exception(e)
            return False


    ####################################################
    # Take electrical reading
    ####################################################

    def take_reading(self):
        
        if not self.as_service:
            #use loop_start() if running as service.  If testing, use this.
            try:
                self.client.loop(.1)
            except:
                time.sleep(10)

        if (time.perf_counter() - self.t_heartbeat > 240) or (time.perf_counter() - self.t_heartbeat < 0):
            self.t_heartbeat = time.perf_counter()
            now = datetime.now()
            current_time = now.strftime("%d/%m/%y   %H:%M:%S")
            try:
                self.client.publish("/emon/heartbeat", self.t_heartbeat, qos=0)
            except:
                logging.warning('emon failed to publish heartbeat')
                time.sleep(5)


        # individual readings
        # self.circuit[?].get_all_readings()
        # self.circuit[X].readings_ray[Y]["metric"]
        #       X       = circuit number (0 to 3 when using two CircuitSetup 6 channel modules)
        #       Y       = channel number (0 to 2), each circuit has 3 channels
        #       metric  = power_active, power_factor, etc...
        
        for x in self.circuit:
            # means self.circuit[0, 1, 2, 3], x=circuit number, iterate through all circuits 
            x.get_all_readings()
            for y in range(len(x.readings_ray)):
                # means x.readings_ray[0, 1, 2], y=channels, iterate through all channels
                publish_flag = False
                if ((x.update_interval[y] == 0.0) or (time.perf_counter() - x.previous_timestamp[y])) > x.update_interval[y]:
                    publish_flag = True
                    x.previous_timestamp[y] = time.perf_counter()
                    if self.debug:
                        print("time stamp for ", x.readings_ray[y]["name"], " @ ", time.perf_counter(), " more than  ", x.update_interval[y], " seconds ago")

                for z in x.readings_ray[y]:
                    # means readings_ray[y]["metric"], z=metric like line_current, power_active, etc..
                    # the first item in list is "name" - don't publish that.
                    if z != "name":
                        # decide if change is great enough
                        if ( abs(x.readings_ray[y][z] - x.readings_previous[y][z]) > x.readings_min_change[y][z]):
                            if self.debug:
                                print("changed!    ", x.readings_ray[y]["name"], "/", str(z), " from ", x.readings_previous[y][z], " to ", x.readings_ray[y][z])
                            x.readings_previous[y][z] = x.readings_ray[y][z]
                            publish_flag = True
                        else:
                            pass
                        
                        # publish the data if 1) update interval exceeded 2) metric value changed enough 3) we're just supposed to always publish
                        if publish_flag or ALWAYS_PUBLISH:
                            mqtt_topic = "/emon/reading/" + x.readings_ray[y]["name"] + "/" + str(z)
                            #print(mqtt_topic)
                            try:
                                self.client.publish(mqtt_topic, x.readings_ray[y][z])
                            except:
                                time.sleep(5)
                            #print(" loop=", y["name"], "  attribute", str(z), " = ", y[z])
                        else:
                            #no publish
                            pass

        return


        
m = Monitor()

m.init_sensor()

while(1):

    #t0= time.perf_counter() 
    m.take_reading()
    #print("read duration = ", time.perf_counter()-t0)
    # it takes 0.25 seconds to take reading and publish on 12 channels.
    
    # *** todo ***
    # Set how frequently to make readings and publish data
    time.sleep(0.5)




 