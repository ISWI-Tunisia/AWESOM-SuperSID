# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Original program: matlab code (LongTermNarrowband.m) by Morris Cohen
Purpose: concatinate longterm AWESOME data (Amplitude NS/EW)
        Tutorial: "Data exercise on geomagnetic activity and narrowband data" by Morris Cohen
        AWESOME workshop, Tunisia 2009.
Inputs: Path to folder, filenames
Outputs: Image 
Date Created: Mon Mar 26 20:00:29 2018
Date Released: Wed Mar 28 20:01:49 2018
Versions:
    V0.01
    
'''
import glob
import scipy.io as mat
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

def ConcatData(pathname="", filename=""):
    
    global Start, Rx_name, Tx_name
    Rx_name='Kodiak'
    Tx_name='NAA'
    AveragingTime = 60
    FileList=glob.glob(pathname+filename)
    FirstFileName= FileList[0]
    LastFileName = FileList[-1]
    LoadFirstData = mat.loadmat(FirstFileName, struct_as_record=False,
                                      squeeze_me=True)
    y1 = int(LoadFirstData['start_year'])
    m1 = int(LoadFirstData['start_month'])
    d1 = int(LoadFirstData['start_day'])
    StartingDate = date.toordinal(date(y1,m1,d1))
    Start = date(y1,m1,d1).strftime("%d. %B %Y")
    print(Start)
    LoadLastData = mat.loadmat(LastFileName, struct_as_record=False,
                                       squeeze_me=True)
    y2 = int(LoadLastData['start_year'])
    m2 = int(LoadLastData['start_month'])
    d2 = int(LoadLastData['start_day'])
    EndingDate = date.toordinal(date(y2,m2,d2))
    End = [y2, m2, d2]
    print(End)
 
    Range = EndingDate-StartingDate+1 # how many days will we be plotting?
    print(Range)
    AmpNS = np.zeros([Range, 1438])     # initialize the matrices into which we will load the data
    AmpEW = np.zeros([Range, 1438])
    
    print(np.shape(AmpNS))
    
    for ii in range(1,len(FileList)):
        CurrentFileName = FileList[ii]
        LoadCurrentData = mat.loadmat(CurrentFileName, struct_as_record=False,
                                       squeeze_me=True)
        y = int(LoadCurrentData['start_year'])
        m = int(LoadCurrentData['start_month'])
        d = int(LoadCurrentData['start_day'])
        h = int(LoadCurrentData['start_hour'])
        mn = int(LoadCurrentData['start_minute'])
        s = int(LoadCurrentData['start_second'])
        data= LoadCurrentData['data']
        adc_channel_number =  LoadCurrentData['adc_channel_number']
        
        CurrentDate = date.toordinal(date(y,m,d))
        StartPoint = 1 + np.mod(AveragingTime-s,AveragingTime)
        InitialMinute = h*60 + mn + s/60
    #    print(StartPoint)
        print(CurrentFileName)
    #    print(len(data))
        for jj in np.arange(StartPoint,(len(data)-AveragingTime-1), AveragingTime):
            a=data[int(jj):int(jj+AveragingTime-1)]
            Average = np.mean(a, axis=0)
    #        print(Average)
            if adc_channel_number == 0:
    #            print(int(InitialMinute + (jj-1)/60))
                AmpNS[CurrentDate-StartingDate+1:, int(InitialMinute + (jj-1)/60):] = Average
                      
            elif adc_channel_number == 1:
                AmpEW[CurrentDate-StartingDate+1:, int(InitialMinute + (jj-1)/60):] = Average
    return Range, AmpNS, AmpEW

# now Plot the data in an image
Range, AmpNS, AmpEW = ConcatData(pathname="H:/NarrowbandData/NAA/", filename="*NAA*A.mat")

fig=plt.figure(figsize=(7.5, 5))

if sum(sum(AmpNS)) >0: # If any data has been loaded then plot it
    fig.add_subplot(1, 2, 1)
    plt.imshow(20*np.log10(AmpNS), interpolation='Nearest', cmap='viridis',
               origin='lower', extent=[0, 24 , 0, Range],aspect='auto',
                                      vmin=15, vmax=45)
    plt.xlabel('Time (UT Hours)', fontsize=10, weight='bold')
    plt.ylabel('Days after ' + Start, fontsize=10, weight='bold')
    plt.title(Tx_name +': N/S Amplitude at '+Rx_name, fontsize=10, weight='bold')
    clb = plt.colorbar()
    clb.set_label('dB (rel)', labelpad=-20, y=1.05, rotation=0, fontsize=8, weight='bold')
    
if sum(sum(AmpEW)) >0:
    fig.add_subplot(1, 2, 2)
    
    plt.imshow(20*np.log10(AmpEW), interpolation='Nearest', cmap='viridis',
               origin='lower', extent=[0, 24 , 0, Range],aspect='auto',
                                      vmin=0, vmax=30)
    
    plt.xlabel('Time (UT Hours)', fontsize=10, weight='bold')
    plt.ylabel('Days after ' + Start, fontsize=10, weight='bold')
    plt.title(Tx_name +': E/W Amplitude at '+Rx_name, fontsize=10, weight='bold')
    clb = plt.colorbar()
    clb.set_label('dB (rel)', labelpad=-20, y=1.05, rotation=0, fontsize=8, weight='bold')
plt.tight_layout()
plt.savefig(Tx_name+"LongTermData"+Rx_name+".png")
plt.show()


