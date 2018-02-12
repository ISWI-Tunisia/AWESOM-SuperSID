import matplotlib.pyplot as plt
import pandas as pd

course_data2 = pd.read_excel("NOAA_Solar_Calculations_day.xls", sheetname='Calculations',
                             infer_datetime_format=True, index_col=4)

plt.figure()
course_data2['Solar Elevation Angle (deg)'].plot(style='r--',linewidth=3, title='Solar Elevation Angle $\chi(^{\circ})$', alpha=0.8)

plt.grid()
plt.savefig("chi.png")

plt.figure()
course_data2['Hprime'].plot(style='g--',linewidth=3, title="$H'(km)$", alpha=0.8)
plt.grid()
plt.savefig("Hp.png")

plt.figure()
course_data2['Beta'].plot(style='b--',linewidth=3, title=r'$\beta (km^{-1})$', alpha=0.8)
plt.grid()
plt.savefig("Beta.png")

#plt.figure()
#course_data2['Approx Atmospheric Refraction (deg)'].plot(style='g--',linewidth=3, title='Approx Atmospheric Refraction (deg)', alpha=0.6)
#plt.grid()

plt.show()
