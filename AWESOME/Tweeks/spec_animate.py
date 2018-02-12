# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:32:07 2016

@author: ahmed
"""
import wave
import sys
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
# DRAW A FIGURE WITH MATPLOTLIB



filename='audioData/Tunisia-2015-10-03-02-00-00-0.wav'
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
duration = 60

fig, ax = plt.subplots(1,figsize=(10, 7), facecolor='white')

    
def update(i, ax, fig):
    
    ax.cla()

    wframe = ax.specgram(signal, NFFT=512, noverlap=300, Fs=fs,vmin=-25, cmap=plt.cm.gnuplot2, interpolation='sinc') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis
    ax.set_ylim(0, 50000)
    ax.set_title(station + ', ' + date + ', ' + CH, fontsize=18, weight='bold')
    ax.set_xlabel("Seconds after " + time + " UT", fontsize=16, weight='bold')
    ax.set_ylabel("Frequency (Hz)", fontsize=16, weight='bold')
    A=i
    B=0.6 + i
    ax.set_xlim(A, B)
    return wframe,

anim = animation.FuncAnimation(fig, update, 
        frames=np.arange(37,55,0.2), 
        fargs=(ax, fig),interval=15)
mywriter = animation.FFMpegWriter(fps=5)
anim.save('mymovie2.mp4',writer=mywriter,fps=5,dpi=150)
#anim.save('animation.gif', writer='imagemagick',fps=5,dpi=80)

