import os
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

os.environ['PROJ_LIB'] = '/home/b08209006/.conda/envs/IONTU/share/proj'
from mpl_toolkits.basemap import Basemap


def Annual_mean(aice, years):
    aice_annual_mean = np.zeros([years, 180, 360])
    for j in range(years):
        aice_annual_mean[j] = sum(aice[j * 12:(j + 1) * 12]) / 12
    return aice_annual_mean


data = xr.open_dataset("/home/b08209006/IONTU/SIC/HadISST_ice.nc")
sic = np.asarray(data['sic'][:-9])
lat = np.asarray(data['latitude'])
lon = np.asarray(data['longitude'])

year = 149
sic_mean = Annual_mean(sic, year)

for i in range(71):
    m = Basemap(projection="ortho", lon_0=120, lat_0=90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, sic_mean[-71+i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Arctic Obs %d" % (i + 1948))
    plt.savefig("Arctic_Obs_%d.png" % (i + 1948))
    plt.show()
    plt.close()

"""
for i in range(71):
    m = Basemap(projection="ortho", lon_0=120, lat_0=-90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, sic_mean[-71+i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Antarctica Obs %d" % (i + 1948))
    plt.savefig("Antarctica_Obs_%d.png" % (i + 1948))
    plt.show()
    plt.close()
"""