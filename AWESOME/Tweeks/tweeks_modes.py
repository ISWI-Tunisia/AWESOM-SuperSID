#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 11:22:45 2017

@author: ahmed
"""

import wave
import sys
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt

def GetSpect(filename):
    global Time; global signal; global fs;
    global station; global date; global CH; global time
    
    time= str(filename[-14:-12]) + ':' + str(filename[-11:-9]) + ':' + str(filename[-8:-6])
    date= str(filename[-17:-15]) + '-' + str(filename[-20:-18]) + '-' + str(filename[-25:-21])
    if filename[-5:-4]=='0':
        CH='NS'
    else:
        CH='EW'
    station = str(filename[-33:-26])
    
    spf = wave.open(filename,'r')
    
    #Extract Raw Audio from Wav File
    signal = spf.readframes(-1)
    signal = np.fromstring(signal, 'Int16')
    fs = spf.getframerate()
    #If Stereo
    if spf.getnchannels() == 2:
        print ('Just mono files')
        sys.exit(0)
    
    Time=np.linspace(0, len(signal)/fs, num=len(signal))
    
GetSpect("audioData/Tunisia-2015-10-01-18-00-00-0.wav")
s1, fs1, station1, date1, time1, CH1=signal,fs,station,date,time, CH

GetSpect("audioData/Tunisia-2015-10-01-21-00-00-0.wav")
s2, fs2, station2, date2, time2, CH2=signal,fs,station,date,time, CH

GetSpect("audioData/Tunisia-2015-10-01-23-00-00-0.wav")
s3, fs3, station3, date3, time3, CH3=signal,fs,station,date,time, CH


'''
plot time-frequency domain:
'''

fig=plt.figure(figsize=(12,8))
ax1=plt.subplot(2,2,1)

ax1.specgram(s1, NFFT=512, noverlap=300,
                 Fs=fs1,vmin=-15, vmax=25,
                 interpolation='hamming') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis

ax1.set_xlim(24.85, 25.15)
ax1.set_ylim(0, 30000)
plt.yticks(np.linspace(0,30000,4),np.linspace(0,30,4))
ax1.set_title(station1 + ', ' + date1 + ', ' + CH1, fontsize=14, weight='bold', color='r')

ax1.set_xlabel("Seconds after " + time1 + " UT", fontsize=12, weight='bold', color='b')
ax1.set_ylabel("Frequency (kHz)", fontsize=12, weight='bold', color='b')
ax1.annotate("n = 3 modes", xy=(24.991, 20000),
                xycoords='data',bbox=dict(boxstyle="round4,pad=.5", fc="w"),
                xytext=(45, 25),color="r",fontsize=11, weight="bold", textcoords='offset points',
                arrowprops=dict(facecolor='r', shrink=0.05),horizontalalignment='center', verticalalignment='center',
                )

ax2=plt.subplot(2,2,2)

ax2.specgram(s2, NFFT=512, noverlap=300,
                 Fs=fs2,vmin=-15, vmax=25,
                 interpolation='hamming') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis

ax2.set_xlim(13.8, 14.1)
ax2.set_ylim(0, 30000)
plt.yticks(np.linspace(0,30000,4),np.linspace(0,30,4))
ax2.set_title(station2 + ', ' + date2 + ', ' + CH2, fontsize=14, weight='bold', color='r')

ax2.set_xlabel("Seconds after " + time2 + " UT", fontsize=12, weight='bold', color='b')
ax2.set_ylabel("Frequency (kHz)", fontsize=12, weight='bold', color='b')
ax2.annotate("n = 6 modes", xy=(13.885, 20000),
                xycoords='data',bbox=dict(boxstyle="round4,pad=.5", fc="w"),
                xytext=(45, 25),color="r",fontsize=11, weight="bold", textcoords='offset points',
                arrowprops=dict(facecolor='r', shrink=0.05),horizontalalignment='center', verticalalignment='center',
                )

ax3=plt.subplot(2,2,3)
ax3.specgram(s3, NFFT=512, noverlap=300,
                 Fs=fs3,vmin=-15, vmax=20,
                 interpolation='hamming') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis

ax3.set_xlim(1.80, 2.1)
ax3.set_ylim(0, 30000)
plt.yticks(np.linspace(0,30000,4),np.linspace(0,30,4))
ax3.set_title(station3 + ', ' + date3 + ', ' + CH3, fontsize=14, weight='bold', color='r')

ax3.set_xlabel("Seconds after " + time3 + " UT", fontsize=12, weight='bold', color='b')
ax3.set_ylabel("Frequency (kHz)", fontsize=12, weight='bold', color='b')
ax3.annotate("n = 5 modes", xy=(1.893, 20000),
                xycoords='data',bbox=dict(boxstyle="round4,pad=.5", fc="w"),
                xytext=(45, 25),color="r",fontsize=11, weight="bold", textcoords='offset points',
                arrowprops=dict(facecolor='r', shrink=0.05),horizontalalignment='center', verticalalignment='center',
                )
ax4=plt.subplot(2,2,4)
ax4.specgram(s3, NFFT=512, noverlap=300,
                 Fs=fs3,vmin=-15, vmax=30,
                 interpolation='hamming') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis

ax4.set_xlim(21.8, 22.05)
ax4.set_ylim(0, 30000)
plt.yticks(np.linspace(0,30000,4),np.linspace(0,30,4))
ax4.set_title(station3 + ', ' + date3 + ', ' + CH3, fontsize=14, weight='bold', color='r')

ax4.set_xlabel("Seconds after " + time3 + " UT", fontsize=12, weight='bold', color='b')
ax4.set_ylabel("Frequency (kHz)", fontsize=12, weight='bold', color='b')
ax4.annotate("n = 2 modes", xy=(21.896, 20000),
                xycoords='data',bbox=dict(boxstyle="round4,pad=.5", fc="w"),
                xytext=(45, 25),color="r",fontsize=11, weight="bold", textcoords='offset points',
                arrowprops=dict(facecolor='r', shrink=0.05),horizontalalignment='center', verticalalignment='center',
                )
plt.tight_layout()
plt.savefig("spectrogram4.pdf")
plt.show()
