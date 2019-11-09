from scipy import signal
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np
import pyqtgraph
from tkinter import filedialog, Tk
## DIMENSION DES FENETRES
# FENETRE PRINCIPALE
tStart_P = 11.58
tEnd_P = 12
AmpMin_P = 0
AmpMax_P = 50000

# Import wav file
root = Tk()
root.withdraw()
filename =  filedialog.askopenfilename(initialdir = ".",title = "Select file",
                                        filetypes = (("audio files","*.wav"),("all files","*.*")))
# read wav file
sample_rate, samples = wavfile.read('Tunisia-2015-10-01-00-00-00-0.wav')
Fs = sample_rate
f, t, Sxx = signal.spectrogram(samples, Fs,nperseg = 265,

                                                    nfft=265, noverlap=100)
# convert signal to dB
Sxx = 20 * np.log(Sxx)
# Interpret image data as row-major instead of col-major
pyqtgraph.setConfigOptions(imageAxisOrder='row-major')

pyqtgraph.mkQApp()
win = pyqtgraph.GraphicsLayoutWidget()
# A plot area (ViewBox + axes) for displaying the image
p1 = win.addPlot()

# Item for displaying image data
img = pyqtgraph.ImageItem()
p1.addItem(img)
# Custom ROI for selecting an image region
roi = pyqtgraph.ROI([11.6, 10000], [0.2, 11000])
roi.addScaleHandle([0.5, 1], [0.5, 0.5])
roi.addScaleHandle([0, 0.5], [0.5, 0.5])
p1.addItem(roi)
roi.setZValue(10)  # make sure ROI is drawn above image

# Add a histogram with which to control the gradient of the image
hist = pyqtgraph.HistogramLUTItem()
# Link the histogram to the image
hist.setImageItem(img)

# If you don't add the histogram to the window, it stays invisible, but I find it useful.
win.addItem(hist)
# Show the window
win.show()
# Fit the min and max levels of the histogram to the data available
hist.setLevels(-200, 250)
# This gradient is roughly comparable to the gradient used by Matplotlib
# You can adjust it and then save it using hist.gradient.saveState()
hist.gradient.restoreState(
        {'mode': 'rgb',
         'ticks': [(0.5, (0, 182, 188, 255)),
                   (1.0, (246, 111, 0, 255)),
                   (0.0, (75, 0, 113, 255))]})
# Sxx contains the amplitude for each pixel
img.setImage(Sxx)
# Scale the X and Y Axis to time and frequency (standard is pixels)
img.scale(t[-1]/np.size(Sxx, axis=1),
          f[-1]/np.size(Sxx, axis=0))
# Limit panning/zooming to the spectrogram
p1.setLimits(xMin=tStart_P, xMax=tEnd_P, yMin=AmpMin_P, yMax=AmpMax_P)
# Add labels to the axis
p1.setLabel('bottom', "Time", units='s')
# If you include the units, Pyqtgraph automatically scales the axis and adjusts the SI prefix (in this case kHz)
p1.setLabel('left', "Frequency", units='Hz')

# Another plot area for displaying ROI data
win.nextRow()
p2 = win.addPlot(colspan=2)
p2.setMaximumHeight(200)
win.resize(800, 600)
win.show()
# Callbacks for handling user interaction
def updatePlot():
    global img, roi, Sxx, p2
    selected = roi.getArrayRegion(Sxx, img)
    p2.plot(selected.mean(axis=0), clear=True)

roi.sigRegionChanged.connect(updatePlot)
updatePlot()

## Plotting with Matplotlib in comparison
#
#plt.pcolormesh(t, f, Sxx, vmin = -200, vmax=200)
#plt.ylabel('Frequency [Hz]')
#plt.xlabel('Time [sec]')
#plt.xlim(tStart_P, tEnd_P)
#plt.ylim(AmpMin_P, AmpMax_P)
#plt.colorbar()
#plt.show()

pyqtgraph.Qt.QtGui.QApplication.instance().exec_()