# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: - - - 
Inputs: - - -
Outputs:  - - -
Date Created: Sun Mar 11 22:50:48 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
    
'''
from LoadData import Load_DAQ_Data
from DAQ_DataPhase import FixDAQ_DataPhase
import numpy as np
import matplotlib.pyplot as plt

def Plot_Data(pathname="", filename=""):
    """
    Plot Amplitude and Phase from AWESOME DATA
    """
    # FIXME: d is a bad variable! Should be fixed
    d=FixDAQ_DataPhase(pathname, filename)
    time, Data, StationInfo =Load_DAQ_Data(d.path, d.filename)
    
    fs=StationInfo['fs']
    if StationInfo['data_type']==1.0:
        Data_amp= Data
        ##Averaging
        AveragingLengthAmp = 20
        data_amp_averaged = np.zeros((len(Data_amp) - AveragingLengthAmp + 1,1),float)
        for jj in range(0, (len(Data_amp)-AveragingLengthAmp+1)):
            data_amp_averaged[jj] = np.mean(Data_amp[jj:(jj+AveragingLengthAmp-1)])
        ## Figure
        plt.figure(figsize=(7.5,5))   
        plt.plot(time[:len(data_amp_averaged)], 20*np.log10(data_amp_averaged), lw=1, color='r')
        plt.plot(time, 20*np.log10(Data_amp), ls='-', lw=.5, color='b', alpha=.5)
        plt.xlabel("Time (UT)", weight = 'bold')
        plt.ylabel("Amplitude (dB)", weight = 'bold')
        plt.show()
    else:
        Data_phi= Data
    
        ##phase unwrapped
        PhaseFixLength90 = 3000
        PhaseFixLength180 =3000
        averaging_length=fs*PhaseFixLength180
    #    print(averaging_length)
        data_phase_fixed180 = d.fix_phasedata180(Data_phi, averaging_length)
    #    print(data_phase_fixed180)
        data_phase_fixed90 = d.fix_phasedata90(data_phase_fixed180, averaging_length)
        data_phase_unwrapped = np.zeros((len(data_phase_fixed90),1),float)
        data_phase_unwrapped[0] = data_phase_fixed90[0]
        
        offset = 0
        for jj in range(1, (len(data_phase_fixed90))):
            if data_phase_fixed90[jj]-data_phase_fixed90[jj-1] > 180:
                offset = offset + 360
            elif data_phase_fixed90[jj]-data_phase_fixed90[jj-1] < -180:
                offset = offset - 360
            data_phase_unwrapped[jj] = data_phase_fixed90[jj] - offset
        
        ##Averaging
        AveragingLengthPhase = 10           
        data_phase_averaged = np.zeros((len(data_phase_unwrapped) - AveragingLengthPhase + 1,1),float)
        for jj in range(0, (len(data_phase_unwrapped) - AveragingLengthPhase + 1)):
            data_phase_averaged[jj] = np.mean(data_phase_unwrapped[jj:(jj+AveragingLengthPhase-1)])
        
        ## Figure
        plt.figure(figsize=(7.5,5)) 
        plt.plot(time[:len(data_phase_averaged)], data_phase_averaged, lw=1, color='r')
        plt.plot(time, data_phase_unwrapped, lw=.5, color='b', alpha=.5)
        plt.xlabel("Time (UT)", weight = 'bold')
        plt.ylabel("Phase (deg)", weight = 'bold')
        plt.show()
if __name__ == "__main__":
    Plot_Data(pathname="H:\\NarrowbandData\\Algeria\\2015\\03\\20\\", filename="*150320*NRK_000A.mat")