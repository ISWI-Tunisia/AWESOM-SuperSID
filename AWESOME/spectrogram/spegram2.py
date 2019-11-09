import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
from scipy.io import wavfile
## DIMENSION DES FENETRES
# FENETRE PRINCIPALE
tStart_P = 11.58
tEnd_P = 12
AmpMin_P = 0
AmpMax_P = 40000
sample_rate, samples = wavfile.read('Tunisia-2015-10-01-00-00-00-0.wav')

Fs = sample_rate

frequencies, times, spectrogram = signal.spectrogram(samples, Fs,nperseg = 512,
                                                     nfft=512, noverlap=100)

spectrogram = 20*np.log(spectrogram)


plt.figure()
plt.pcolormesh(times, frequencies, spectrogram, vmin = 0, vmax=100)
# plt.imshow(spectrogram)
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.xlim(tStart_P, tEnd_P)
plt.ylim(AmpMin_P, AmpMax_P)
plt.colorbar()
plt.show()