# -*- coding: utf-8 -*-
'''
Author: Ahmed Ammar, ahmed.ammar@fst.utm.tn
Purpose: concatinate data
Inputs: - - -
Outputs:  - - -
Date Created: Mon Mar 26 20:00:29 2018
Date Modified: M D, Y
Date Released: M D, Y
Versions:
    V0.01: ---
    
'''
import glob
import scipy.io as mat
from datetime import date
import numpy as np
import matplotlib.pyplot as plt

def ConcatData(pathname="", filename=""):
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
    Start = [y1, m1, d1]
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
            Average = a.mean(axis=0)
    #        print(Average)
            if adc_channel_number == 0:
    #            print(int(InitialMinute + (jj-1)/60))
                AmpNS[CurrentDate-StartingDate+1:, int(InitialMinute + (jj-1)/60):] = Average
                      
            elif adc_channel_number == 1:
                AmpEW[CurrentDate-StartingDate+1:, int(InitialMinute + (jj-1)/60):] = Average
    return Range, AmpNS, AmpEW

# now Plot the data in an image
Range, AmpNS, AmpEW = ConcatData(pathname="H:/NarrowbandData/Tunisia/2017/09/NRK/", filename="*NRK*A.mat")

fig=plt.figure(figsize=(7.5, 5))
fig.add_subplot(1, 2, 1)

plt.imshow(20*np.log10(AmpNS), interpolation='nearest', cmap='rainbow',
           origin='lower', extent=[0, 24 , 0, Range],aspect='auto')

plt.colorbar()
fig.add_subplot(1, 2, 2)

plt.imshow(20*np.log10(AmpEW), interpolation='gaussian', cmap='rainbow',
           origin='lower', extent=[0, 24 , 0, Range],aspect='auto')

plt.colorbar()
plt.tight_layout()
plt.show()


