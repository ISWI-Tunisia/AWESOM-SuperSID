# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 13:42:34 2016

@author: ahmed
"""

import wave
import sys
import numpy as np
import matplotlib.pyplot as plt
'''
signal1 waveform of the NS antenna 
'''
filename1='audioData/Tunisia-2015-10-01-00-00-00-0.wav'
time= str(filename1[-14:-12]) + ':' + str(filename1[-11:-9]) + ':' + str(filename1[-8:-6])
date= str(filename1[-17:-15]) + '-' + str(filename1[-20:-18]) + '-' + str(filename1[-25:-21])
if filename1[-5:-4]=='0':
    CH1='NS'
else:
    CH1='EW'
station = str(filename1[-33:-26])

spf1 = wave.open(filename1,'r')

#Extract Raw Audio from Wav File
signal1 = spf1.readframes(-1)
signal1 = np.fromstring(signal1, 'Int16')
fs1 = spf1.getframerate()
#If Stereo
if spf1.getnchannels() == 2:
    print ('Just mono files')
    sys.exit(0)

Time1=np.linspace(0, len(signal1)/fs1, num=len(signal1))

'''
signal2= waveform of the EW antenna 
'''
filename2='audioData/Tunisia-2015-10-01-00-00-00-1.wav'

if filename2[-5:-4]=='0':
    CH2='NS'
else:
    CH2='EW'

spf2 = wave.open(filename2,'r')

#Extract Raw Audio from Wav File
signal2 = spf2.readframes(-1)
signal2 = np.fromstring(signal2, 'Int16')
fs2 = spf2.getframerate()
#If Stereo
if spf2.getnchannels() == 2:
    print ('Just mono files')
    sys.exit(0)

Time2=np.linspace(0, len(signal2)/fs2, num=len(signal2))

'''
Plot signals
'''

plt.figure(figsize=(7, 4), facecolor='white',dpi=100)
plt.plot(Time1,signal1, linewidth=3,label=CH1 )
plt.plot(Time1,signal2, linewidth=3,label=CH2 )


plt.title(station + ', ' + date, fontsize=18, weight='bold')
plt.xlabel("Seconds after " + time + " UT", fontsize=16, weight='bold')

plt.legend()
plt.savefig(filename1[:-4] + '.pdf')
plt.show()
