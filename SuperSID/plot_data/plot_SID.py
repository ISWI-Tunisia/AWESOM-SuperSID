import matplotlib.pyplot as plt
import numpy as np

dataNAA = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_NAA_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])

data_length = len(dataNAA) #
time_data   = np.arange(0.0, 24.0 , 24.0/(1.0 * data_length))

dataICV = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_ICV_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])

dataGQD = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_GQD_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])
dataNSY = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_NSY_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])
dataGBZ = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_GBZ_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])
                  
dataDHO = np.loadtxt("SuperSID_data/LSAMA-Tunisia_271_DHO_2014-10-22T00.00.00.txt",
                  comments='#', delimiter=",", skiprows=12, usecols=[1])


dataGOES = np.loadtxt("goes_data/20141022_Gp_xr_5m.txt", skiprows=18, usecols=[7])
data_length2 = len(dataGOES) #
time_data2   = np.arange(0.0, 24.0 , 24.0/(1.0 * data_length2))

plt.plot(time_data, dataNAA/max(dataNAA),linewidth=3,label="NAA(24 kHz)",alpha=.8)
plt.plot(time_data, dataICV/max(dataICV),linewidth=3,label="ICV(20.27 kHz)",alpha=.8)
plt.plot(time_data, dataGQD/max(dataGQD),linewidth=3,label="GQD(22.10 kHz)",alpha=.8)
plt.plot(time_data, dataNSY/max(dataNSY),linewidth=3,label="NSC(45.9 kHz)",alpha=.8)
plt.plot(time_data, dataGBZ/max(dataGBZ),linewidth=3,label="GBZ(19.60 kHz)",alpha=.8)
plt.plot(time_data, dataDHO/max(dataDHO),linewidth=3,label="DHO(23.40 kHz)",alpha=.8)

plt.legend(loc='upper left')
plt.xlabel("Time(UT)")
plt.ylabel("Normalized VLF amplitude")
ax2 = plt.twinx()
ax2.plot(time_data2, dataGOES,color='k',linewidth=3,label="GOES X Ray")
ax2.set_yscale('log')
ax2.set_ylabel("X ray Flux (0.1 - 0.8 nanometer)")
plt.legend()
plt.tight_layout()
plt.show()

#------------------------------
#-----------------------------
