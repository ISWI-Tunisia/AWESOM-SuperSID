# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 21:20:05 2016

@author: ahmed
"""

import matplotlib.pyplot as plt
import numpy as np

dataGOESS,dataGOESL = np.loadtxt("goes_data/20141022_Gp_xr_5m.txt", skiprows=18, usecols=[6,7],unpack=True)
data_length2 = len(dataGOESL) #
time_data2   = np.arange(0.0, 24.0 , 24.0/(1.0 * data_length2))
plt.figure(figsize=(10, 7))
plt.plot(time_data2, dataGOESL,color='r',linewidth=3,label="GOES-15: Long X-Ray (0.1 - 0.8 nanometer)")
plt.plot(time_data2, dataGOESS,color='k',linewidth=3,label="GOES-15: Short X-Ray (0.05 - 0.4 nanometer)", alpha=.3)
plt.title(" GOES-15 Solar X-ray Flux, 2014 Oct 22", fontsize=16, weight="bold" )
plt.yscale('log')
plt.ylabel("X ray Flux ($Watts/m^2$)")
plt.legend(loc='upper left')
plt.tight_layout()
plt.grid()
plt.savefig("GOES-15.pdf")
plt.show()