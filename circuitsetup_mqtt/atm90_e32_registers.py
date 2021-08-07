#  REGISTERS *
"""Mappings of the atm90e32 to user readable strings.
"""
# STATUS REGISTERS *#
MeterEn = 0x00   # Metering Enable
ChannelMapI = 0x01  # Current Channel Mapping Configuration
ChannelMapU = 0x02  # Voltage Channel Mapping Configuration
SagPeakDetCfg = 0x05  # Sag and Peak Detector Period Configuration
OVth = 0x06    # Over Voltage Threshold
ZXConfig = 0x07   # Zero-Crossing Config
SagTh = 0x08    # Voltage Sag Th
PhaseLossTh = 0x09  # Voltage Phase Losing Th
INWarnTh = 0x0A   # Neutral Current (Calculated) Warning Threshold
OIth = 0x0B    # Over Current Threshold
FreqLoTh = 0x0C  # Low Threshold for Frequency Detection
FreqHiTh = 0x0D  # High Threshold for Frequency Detection
PMPwrCtrl = 0x0E  # Partial Measurement Mode Power Control
IRQ0MergeCfg = 0x0F  # IRQ0 Merge Configuration
ENStatus0 = 0x95  # Tells us if readings are above the threshold and being read


#  EMM STATUS REGISTERS *#
SoftReset = 0x70  # Software Reset
EMMState0 = 0x71  # EMM State 0
EMMState1 = 0x72  # EMM State 1
EMMIntState0 = 0x73   # EMM Interrupt Status 0
EMMIntState1 = 0x74   # EMM Interrupt Status 1
EMMIntEn0 = 0x75  # EMM Interrupt Enable 0
EMMIntEn1 = 0x76  # EMM Interrupt Enable 1
LastSPIData = 0x78  # Last Read/Write SPI Value
CRCErrStatus = 0x79  # CRC Error Status
CRCDigest = 0x7A  # CRC Digest
CfgRegAccEn = 0x7F  # Configure Register Access Enable

#  LOW POWER MODE REGISTERS - NOT USED *#
DetectCtrl = 0x10
DetectTh1 = 0x11
DetectTh2 = 0x12
DetectTh3 = 0x13
PMOffsetA = 0x14
PMOffsetB = 0x15
PMOffsetC = 0x16
PMPGA = 0x17
PMIrmsA = 0x18
PMIrmsB = 0x19
PMIrmsC = 0x1A
PMConfig = 0x10B
PMAvgSamples = 0x1C
PMIrmsLSB = 0x1D

#  CONFIGURATION REGISTERS *#
PLconstH = 0x31   # High Word of PL_Constant
PLconstL = 0x32   # Low Word of PL_Constant
MMode0 = 0x33   # Metering Mode Config
MMode1 = 0x34   # PGA Gain Configuration for Current Channels
PStartTh = 0x35   # Startup Power Th (P)
QStartTh = 0x36   # Startup Power Th (Q)
SStartTh = 0x37  # Startup Power Th (S)
PPhaseTh = 0x38   # Startup Power Accum Th (P)
QPhaseTh = 0x39  # Startup Power Accum Th (Q)
SPhaseTh = 0x3A  # Startup Power Accum Th (S)

#  CALIBRATION REGISTERS *#
PoffsetA = 0x41   # A Line Power Offset (P)
QoffsetA = 0x42   # A Line Power Offset (Q)
PoffsetB = 0x43   # B Line Power Offset (P)
QoffsetB = 0x44   # B Line Power Offset (Q)
PoffsetC = 0x45   # C Line Power Offset (P)
QoffsetC = 0x46   # C Line Power Offset (Q)
PQGainA = 0x47   # A Line Calibration Gain
PhiA = 0x48     # A Line Calibration Angle
PQGainB = 0x49   # B Line Calibration Gain
PhiB = 0x4A     # B Line Calibration Angle
PQGainC = 0x4B   # C Line Calibration Gain
PhiC = 0x4C     # C Line Calibration Angle

#  FUNDAMENTAL#HARMONIC ENERGY CALIBRATION REGISTERS *#
POffsetAF = 0x51  # A Fund Power Offset (P)
POffsetBF = 0x52  # B Fund Power Offset (P)
POffsetCF = 0x53  # C Fund Power Offset (P)
PGainAF = 0x54  # A Fund Power Gain (P)
PGainBF = 0x55  # B Fund Power Gain (P)
PGainCF = 0x56  # C Fund Power Gain (P)

#  MEASUREMENT CALIBRATION REGISTERS *#
UgainA = 0x61   # A Voltage RMS Gain
IgainA = 0x62   # A Current RMS Gain
UoffsetA = 0x63   # A Voltage Offset
IoffsetA = 0x64   # A Current Offset
UgainB = 0x65   # B Voltage RMS Gain
IgainB = 0x66   # B Current RMS Gain
UoffsetB = 0x67   # B Voltage Offset
IoffsetB = 0x68   # B Current Offset
UgainC = 0x69   # C Voltage RMS Gain
IgainC = 0x6A   # C Current RMS Gain
UoffsetC = 0x6B   # C Voltage Offset
IoffsetC = 0x6C   # C Current Offset
IoffsetN = 0x6E   # N Current Offset

#  ENERGY REGISTERS *#
APenergyT = 0x80   # Total Forward Active
APenergyA = 0x81   # A Forward Active
APenergyB = 0x82   # B Forward Active
APenergyC = 0x83   # C Forward Active
ANenergyT = 0x84   # Total Reverse Active
ANenergyA = 0x85   # A Reverse Active
ANenergyB = 0x86   # B Reverse Active
ANenergyC = 0x87   # C Reverse Active
RPenergyT = 0x88   # Total Forward Reactive
RPenergyA = 0x89   # A Forward Reactive
RPenergyB = 0x8A   # B Forward Reactive
RPenergyC = 0x8B   # C Forward Reactive
RNenergyT = 0x8C   # Total Reverse Reactive
RNenergyA = 0x8D   # A Reverse Reactive
RNenergyB = 0x8E   # B Reverse Reactive
RNenergyC = 0x8F   # C Reverse Reactive

SAenergyT = 0x90   # Total Apparent Energy
SenergyA = 0x91    # A Apparent Energy
SenergyB = 0x92   # B Apparent Energy
SenergyC = 0x93   # C Apparent Energy


#  FUNDAMENTAL # HARMONIC ENERGY REGISTERS *#
APenergyTF = 0xA0  # Total Forward Fund. Energy
APenergyAF = 0xA1  # A Forward Fund. Energy
APenergyBF = 0xA2  # B Forward Fund. Energy
APenergyCF = 0xA3  # C Forward Fund. Energy
ANenergyTF = 0xA4   # Total Reverse Fund Energy
ANenergyAF = 0xA5  # A Reverse Fund. Energy
ANenergyBF = 0xA6  # B Reverse Fund. Energy
ANenergyCF = 0xA7  # C Reverse Fund. Energy
APenergyTH = 0xA8  # Total Forward Harm. Energy
APenergyAH = 0xA9  # A Forward Harm. Energy
APenergyBH = 0xAA  # B Forward Harm. Energy
APenergyCH = 0xAB  # C Forward Harm. Energy
ANenergyTH = 0xAC  # Total Reverse Harm. Energy
ANenergyAH = 0xAD   # A Reverse Harm. Energy
ANenergyBH = 0xAE   # B Reverse Harm. Energy
ANenergyCH = 0xAF   # C Reverse Harm. Energy

#  POWER & P.F. REGISTERS *#
PmeanT = 0xB0   # Total Mean Power (P)
PmeanA = 0xB1   # A Mean Power (P)
PmeanB = 0xB2   # B Mean Power (P)
PmeanC = 0xB3   # C Mean Power (P)
QmeanT = 0xB4   # Total Mean Power (Q)
QmeanA = 0xB5   # A Mean Power (Q)
QmeanB = 0xB6   # B Mean Power (Q)
QmeanC = 0xB7   # C Mean Power (Q)
SmeanT = 0xB8   # Total Mean Power (S)
SmeanA = 0xB9   # A Mean Power (S)
SmeanB = 0xBA   # B Mean Power (S)
SmeanC = 0xBB   # C Mean Power (S)
PFmeanT = 0xBC   # Mean Power Factor
PFmeanA = 0xBD   # A Power Factor
PFmeanB = 0xBE   # B Power Factor
PFmeanC = 0xBF   # C Power Factor

PmeanTLSB = 0xC0   # Lower Word (Tot. Act. Power)
PmeanALSB = 0xC1   # Lower Word (A Act. Power)
PmeanBLSB = 0xC2   # Lower Word (B Act. Power)
PmeanCLSB = 0xC3   # Lower Word (C Act. Power)
QmeanTLSB = 0xC4   # Lower Word (Tot. React. Power)
QmeanALSB = 0xC5   # Lower Word (A React. Power)
QmeanBLSB = 0xC6   # Lower Word (B React. Power)
QmeanCLSB = 0xC7   # Lower Word (C React. Power)
SAmeanTLSB = 0xC8  # Lower Word (Tot. App. Power)
SmeanALSB = 0xC9   # Lower Word (A App. Power)
SmeanBLSB = 0xCA   # Lower Word (B App. Power)
SmeanCLSB = 0xCB   # Lower Word (C App. Power)

#  FUND#HARM POWER & V#I RMS REGISTERS *#
PmeanTF = 0xD0   # Total Active Fund. Power
PmeanAF = 0xD1   # A Active Fund. Power
PmeanBF = 0xD2   # B Active Fund. Power
PmeanCF = 0xD3   # C Active Fund. Power
PmeanTH = 0xD4   # Total Active Harm. Power
PmeanAH = 0xD5   # A Active Harm. Power
PmeanBH = 0xD6   # B Active Harm. Power
PmeanCH = 0xD7   # C Active Harm. Power
UrmsA = 0xD9    # A RMS Voltage
UrmsB = 0xDA    # B RMS Voltage
UrmsC = 0xDB    # C RMS Voltage
IrmsA = 0xDD    # A RMS Current
IrmsB = 0xDE    # B RMS Current
IrmsC = 0xDF    # C RMS Current
IrmsN = 0xD8    # Calculated N RMS Current

PmeanTFLSB = 0xE0  # Lower Word (Tot. Act. Fund. Power)
PmeanAFLSB = 0xE1  # Lower Word (A Act. Fund. Power)
PmeanBFLSB = 0xE2  # Lower Word (B Act. Fund. Power)
PmeanCFLSB = 0xE3  # Lower Word (C Act. Fund. Power)
PmeanTHLSB = 0xE4  # Lower Word (Tot. Act. Harm. Power)
PmeanAHLSB = 0xE5  # Lower Word (A Act. Harm. Power)
PmeanBHLSB = 0xE6  # Lower Word (B Act. Harm. Power)
PmeanCHLSB = 0xE7  # Lower Word (C Act. Harm. Power)
# 0xE8	    ## Reserved Register
UrmsALSB = 0xE9  # Lower Word (A RMS Voltage)
UrmsBLSB = 0xEA  # Lower Word (B RMS Voltage)
UrmsCLSB = 0xEB  # Lower Word (C RMS Voltage)
# 0xEC	    ## Reserved Register
IrmsALSB = 0xED  # Lower Word (A RMS Current)
IrmsBLSB = 0xEE  # Lower Word (B RMS Current)
IrmsCLSB = 0xEF  # Lower Word (C RMS Current)

#  THD, FREQUENCY, ANGLE & TEMPTEMP REGISTERS*#
THDNUA = 0xF1   # A Voltage THD+N
THDNUB = 0xF2   # B Voltage THD+N
THDNUC = 0xF3   # C Voltage THD+N
# 0xF4	    ## Reserved Register
THDNIA = 0xF5   # A Current THD+N
THDNIB = 0xF6   # B Current THD+N
THDNIC = 0xF7   # C Current THD+N
Freq = 0xF8    # Frequency
PAngleA = 0xF9   # A Mean Phase Angle
PAngleB = 0xFA   # B Mean Phase Angle
PAngleC = 0xFB   # C Mean Phase Angle
Temp = 0xFC   # Measured Temperature
UangleA = 0xFD  # A Voltage Phase Angle
UangleB = 0xFE  # B Voltage Phase Angle
UangleC = 0xFF  # C Voltage Phase Angle
