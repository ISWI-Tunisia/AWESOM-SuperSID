
#Tunis coordinate
tunis_lat=36.5
tunis_lon=10.08
# --- Build Map ---
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
#from matplotlib.widgets import Cursor
import numpy as np
from datetime import datetime
map = plt.figure(figsize=[10,7]) 
map = Basemap(projection='robin', area_thresh = 1000.0,
              lat_0=0, lon_0=10, resolution = 'l', suppress_ticks=True)      #resolution : 'l' for low and 'h' for hight and 'c'


map.drawcoastlines(color='#A3A3A3')
map.drawcountries(color='#A3A3A3')
map.drawmapboundary(fill_color='lightblue')
map.fillcontinents(color='#FFFFFF',lake_color='lightblue')
map.drawparallels(np.arange(-90,100,30),labels=[1,0,0,0],color='#A1A866', linewidth=.2)
map.drawmeridians(np.arange(map.lonmin,map.lonmax+40,60),labels=[0,0,0,1],color='#A1A866', linewidth=.2)
WWLLN_lons=014.1805
WWLLN_lats=36.7364
x,y = map(WWLLN_lons, WWLLN_lats)
v,w = map(tunis_lon, tunis_lat)

map.plot(v, w, 'bo', markersize=10, label='VLF Reciever')
plt.text(v, w, "Tunis", color='k',fontsize=12, fontweight='bold')
map.plot(x, y, 'ro', markersize=10, label='VLF WWLLN flash')
 
# shade the night areas, with alpha transparency so the
# map shows through. Use current time in UTC.
#date = datetime.today()
date=datetime(2015,10, 1,00)
CS=map.nightshade(date)
#plt.title('Day/Night Map for %s (UT)' % date.strftime("%d %b %Y %H:%M:%S"),fontsize=14, fontweight='bold')
plt.title("Day/Night Map" ,fontsize=14, fontweight='bold')

#to show long/lat coordination under the curosor
ax = plt.gca()
def format_coord(x, y):
    return 'Longitude=%.4f, Latitude=%.4f'%(map(x, y, inverse = True))
ax.format_coord = format_coord

#Circle ref:https://github.com/urschrei/Circles
from circles import circle
from shapely.geometry import Polygon, Point
from descartes import PolygonPatch

radius = 328
centerlon = tunis_lon
centerlat = tunis_lat

# initialise a point and construct a buffered polygon
p = Point(map(centerlon, centerlat))
buffered = p.buffer(radius * 1000)

# same radius, but with calculated coordinates
casa = circle(map, centerlon, centerlat, radius)
pol = Polygon(casa)

# draw circles
correct = PolygonPatch(pol, fc='red', ec='k', alpha=.2, zorder=3)
ax.add_patch(correct)

# with apologies to the Sugababes
#plt.tight_layout()

#make legend
legend = plt.legend(loc='lower left',fontsize=8,frameon=True,title='Legend',markerscale=1,prop={'size':10})
legend.get_title().set_fontsize('20')
plt.savefig("vlf_map.pdf", dps=50)
plt.savefig("vlf_map.png", dps=50)
plt.show()
