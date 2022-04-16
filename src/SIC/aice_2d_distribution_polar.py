import os
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import matplotlib.cm as cm

os.environ['PROJ_LIB'] = '/home/b08209006/.conda/envs/IONTU/share/proj'
from mpl_toolkits.basemap import Basemap


def Annual_mean(aice, years):
    aice_annual_mean = np.zeros([years, 288, 320])
    for j in range(years):
        aice_annual_mean[j] = sum(aice[j * 12:(j + 1) * 12]) / 12
    return aice_annual_mean


data_area = sio.loadmat("/home/b08209006/IONTU/SIC/areaGd.mat")
areaGd = np.asarray(data_area['areaGd']).swapaxes(0, 1)

data_IAF = xr.open_dataset("aice_omip2_yht_GTIAF_QVOLa.nc")
aice_IAF = np.asarray(data_IAF['aice'])
lat = np.asarray(data_IAF['lat'])
lon = np.asarray(data_IAF['lon'])

data_JRA = xr.open_dataset("/home/b08209006/IONTU/SIC/aice_omip2_yht_GTJRA_QVOLa.nc")
aice_JRA = np.asarray(data_JRA['aice'])

year_IAF = 372
aice_IAF = Annual_mean(aice_IAF, year_IAF)
aice_IAF /= 100
aice_IAF_area_array = aice_IAF * areaGd

year_JRA = 366
aice_JRA = Annual_mean(aice_JRA, year_JRA)
aice_JRA /= 100
aice_JRA_area_array = aice_JRA * areaGd
"""
for i in range(62):
    m = Basemap(projection="ortho", lon_0=120, lat_0=90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, aice_IAF[310 + i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Arctic IAF %d" % (i + 1948))
    plt.savefig("Arctic_IAF_%d.png" % (i + 1948))
    plt.show()
    plt.close()

for i in range(61):
    m = Basemap(projection="ortho", lon_0=120, lat_0=90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, aice_JRA[305 + i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Arctic JRA %d" % (i + 1958))
    plt.savefig("Arctic_JRA_%d.png" % (i + 1958))
    plt.show()
    plt.close()
"""
for i in range(62):
    m = Basemap(projection="ortho", lon_0=120, lat_0=-90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, aice_IAF[310 + i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Antarctica IAF %d" % (i + 1948))
    plt.savefig("Antarctica_IAF_%d.png" % (i + 1948))
    plt.show()
    plt.close()

for i in range(61):
    m = Basemap(projection="ortho", lon_0=120, lat_0=-90)
    m.drawcoastlines()
    parallels = np.arange(-90., 90, 30.)
    m.drawparallels(parallels)  # draw parallels 畫緯度線
    meridians = np.arange(0., 360., 20.)
    m.drawmeridians(meridians)  # draw meridians 畫經度線

    lon2, lat2 = np.meshgrid(lon, lat)
    cx, cy = m(lon2, lat2)
    CS = plt.contourf(cx, cy, aice_JRA[305 + i], cmap=cm.Blues, levels=np.arange(0, 1+0.1, 0.1))
    plt.colorbar(CS, orientation="vertical")
    plt.title("Antarctica JRA %d" % (i + 1958))
    plt.savefig("Antarctica_JRA_%d.png" % (i + 1958))
    plt.show()
    plt.close()
