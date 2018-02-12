# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ahmed AMMAR
"""

import wave
import sys
import numpy as np
from scipy.fftpack import fft
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import zoomed_inset_axes,inset_axes
from mpl_toolkits.axes_grid1.inset_locator import mark_inset
from matplotlib.ticker import FormatStrFormatter
filename='audioData/Tunisia-2015-10-05-00-00-00-0.wav'
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
#'''
#plot time-frequency domain:
#'''
#
#fig, ax = plt.subplots(figsize=(10, 6), facecolor='white',dpi=100)
#spec=ax.specgram(signal, NFFT=512, noverlap=300,
#                 Fs=fs,vmin=-15,
#                 interpolation='hamming') #noverlap=250 for low resolution 
##and noverlap=450 for hight resolution, cmap=plt.cm.viridis
#
#ax.set_xlim(34.3, 35.)
#ax.set_ylim(0, 40000)
#plt.yticks(np.linspace(0,40000,5),np.linspace(0,40,5))
#ax.set_title(station + ', ' + date + ', ' + CH, fontsize=18, weight='bold')
#ax.set_xlabel("Seconds after " + time + " UT", fontsize=16, weight='bold')
#ax.set_ylabel("Frequency (kHz)", fontsize=16, weight='bold')
#
##axcb=plt.colorbar(pad=0.05,shrink=1,extendrect=True)
##axcb.set_label('dB', fontsize=14, weight='bold')
#
#
#axins = zoomed_inset_axes(ax, 2, loc=1,borderpad=0.5)  # zoom = 6
#axins.specgram(signal, NFFT=512, noverlap=400, Fs=fs,vmin=10, interpolation='hamming')
#
## sub region of the original image
#x1, x2, y1, y2 = 34.6577, 34.7363, 0, 15000
#
#axins.set_xlim(x1, x2)
#axins.set_ylim(y1, y2)
#plt.xticks(visible=True, fontsize=8, color='w', weight='bold')
#plt.yticks(np.linspace(0,15000,4),np.linspace(0,15,4), visible=True, fontsize=8, color='w', weight='bold')
#plt.axvline(x=34.672, color='w', linestyle='--',alpha=0.5)
#plt.axvline(x=34.6785, color='r', linestyle='--',alpha=0.5)
#plt.axhline(y=1500, color='w', linestyle='--', alpha=0.5)
#plt.plot(34.6785,1700,'xk', ms=5)
#plt.text(34.681,1700,r'$f_2$', color='w',fontsize=12, weight="bold")
#plt.plot(34.672,2000,'xk', ms=5)
#plt.text(34.6735,2100,r'$f_1$', color='w',fontsize=12, weight="bold")
#plt.axhline(y=3200, color='w', linestyle='--', alpha=0.5)
#plt.axhline(y=5100, color='w', linestyle='--', alpha=0.5)
#plt.axhline(y=6800, color='w', linestyle='--', alpha=0.5)
#
#
## draw a bbox of the region of the inset axes in the parent axes and
## connecting lines between the bbox and the inset axes area
#mark_inset(ax, axins, loc1=1, loc2=2, fc="none", ec="1")
#axins.annotate('m = 4 modes', xy=(34.73, 12500),
#                xycoords='data',
#                xytext=(0, 10),color="y",fontsize=9, weight="bold", textcoords='offset points',
#                horizontalalignment='right', verticalalignment='bottom',
#                )
#axins.annotate(u'$f_{c1}$', xy=(34.665, 1450),
#                xycoords='data',
#                xytext=(0, 10),color="w",fontsize=12, weight="bold", textcoords='offset points',
#                horizontalalignment='center', verticalalignment='center',
#                )
#axins.annotate(u'$f_{c2}$', xy=(34.665, 3150),
#                xycoords='data',
#                xytext=(0, 10),color="w",fontsize=12, weight="bold", textcoords='offset points',
#                horizontalalignment='center', verticalalignment='center',
#                )
#axins.annotate(u'$f_{c3}$', xy=(34.665, 5000),
#                xycoords='data',
#                xytext=(0, 10),color="w",fontsize=12, weight="bold", textcoords='offset points',
#                horizontalalignment='center', verticalalignment='center',
#                )
#axins.annotate(u'$f_{c4}$', xy=(34.665, 6750),
#                xycoords='data',
#                xytext=(0, 10),color="w",fontsize=12, weight="bold", textcoords='offset points',
#                horizontalalignment='center', verticalalignment='center',
#                )
#
#axins.annotate(u'$t_1$', xy=(34.672, 0),
#                xycoords='data', bbox=dict(boxstyle="round4,pad=.5", fc="w"),
#                xytext=(-45, 25),color="k",fontsize=12, weight="bold", textcoords='offset points',
#                arrowprops=dict(facecolor='w', shrink=0.05),horizontalalignment='center', verticalalignment='center',
#                )
#axins.annotate(u'$t_2$', xy=(34.6785, 0),
#                xycoords='data',bbox=dict(boxstyle="round4,pad=.5", fc="w"),
#                xytext=(45, 25),color="r",fontsize=12, weight="bold", textcoords='offset points',
#                arrowprops=dict(facecolor='r', shrink=0.05),horizontalalignment='center', verticalalignment='center',
#                )
#
#plt.tight_layout()
#plt.savefig(filename[:-4] + 'TFd' +'.pdf')
#plt.savefig(filename[:-4] + 'TFd' +'.png')
'''
Plot time-domain
'''

plt.figure(figsize=(9, 5), facecolor='white',dpi=100)
plt.plot(Time,signal, linewidth=2 )
plt.xlim(6.85, 6.95)
plt.title(station + ', ' + date, fontsize=18, weight='bold')
plt.xlabel("Seconds after " + time + " UT", fontsize=16, weight='bold')

plt.savefig(filename[:-4] + 'Td' +'.pdf')
plt.savefig(filename[:-4] + 'Td' +'.png')

'''
Plot frequency-domain:
'''

signal2=[]
for i in range(len(Time)):
    if 6.896<=Time[i]<6.902:
        sig=signal[i]
        signal2.append(sig)
def nextpow2(n):
    m_f = np.log2(n)
    m_i = np.ceil(m_f)
    return int(np.log2(2**m_i))
NFFT = 2**nextpow2(len(signal2))
freq =fs/2*np.linspace(0,1,NFFT-1)
FFT_f = fft(signal2,NFFT)
FFT_f = FFT_f[1:NFFT]
plt.figure(figsize=(9, 5), facecolor='white',dpi=100)
mag=abs(FFT_f)/len(signal2)
plt.plot(freq/1e3, mag, linewidth=3 )
plt.xlim(1.2, 10)
plt.ylim(0, max(mag)+20)
plt.xlabel("Frequency (kHz)", fontsize=16, weight='bold')
plt.savefig(filename[:-4] + 'Fd' +'.pdf')
plt.savefig(filename[:-4] + 'Fd' +'.png')
plt.show()
