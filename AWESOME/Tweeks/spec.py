import wave
import sys
import numpy as np
import matplotlib.pyplot as plt

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
plt.figure(figsize=(10, 5), facecolor='white',dpi=100)
spec=plt.specgram(signal, NFFT=512, noverlap=300, Fs=fs,vmin=-25, cmap=plt.cm.gnuplot2, interpolation='sinc') #noverlap=250 for low resolution 
#and noverlap=450 for hight resolution, cmap=plt.cm.viridis

plt.xlim(50., 50.6)
plt.ylim(0, 50000)
plt.title(station + ', ' + date + ', ' + CH, fontsize=18, weight='bold')
plt.xlabel("Seconds after " + time + " UT", fontsize=16, weight='bold')
plt.ylabel("Frequency (Hz)", fontsize=16, weight='bold')

axcb=plt.colorbar(pad=0.05,shrink=1,extendrect=True)
axcb.set_label('dB', fontsize=14, weight='bold')
plt.tight_layout()
plt.savefig(filename[:-4] + '.pdf')
plt.show()
