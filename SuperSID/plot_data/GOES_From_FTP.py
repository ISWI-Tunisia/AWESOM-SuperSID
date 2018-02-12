import numpy as np
import matplotlib.pyplot as plt
import urllib.request
url="http://legacy-www.swpc.noaa.gov/ftpdir/lists/xray/20170906_Gs_xr_5m.txt"
# If you wish to retrieve a resource via URL and store it in a temporary location,
# you can do so via the urlretrieve() function:
local_filename, headers = urllib.request.urlretrieve(url)
file = open(local_filename)
dataGOESS,dataGOESL =np.loadtxt(file, skiprows=18, usecols=[6,7],unpack=True)

data_length2 = len(dataGOESL) #
time_data2   = np.arange(0.0, 24.0 , 24.0/(1.0 * data_length2))
plt.figure()
plt.plot(time_data2, dataGOESL,color='r',linewidth=3,label="GOES-15: Long X-Ray (0.1 - 0.8 nanometer)")
plt.plot(time_data2, dataGOESS,color='k',linewidth=3,label="GOES-15: Short X-Ray (0.05 - 0.4 nanometer)", alpha=.3)
plt.title(" GOES-15 Solar X-ray Flux", fontsize=16, weight="bold" )
plt.yscale('log')
plt.ylabel("X ray Flux ($Watts/m^2$)")
plt.ylim(1E-8,1E-2)
plt.legend(loc='upper left')
plt.tight_layout()
plt.grid()
#plt.savefig("GOES-15.pdf")
plt.show()
