import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.cm as cm
import cartopy.feature as cfeature
import matplotlib as mpl
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

data_IAF = xr.open_dataset("/home/b08209006/IONTU/BSF/IAF_msftbarot/gn/msftbarot_Omon_TaiESM1"
                           "-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc", decode_times=False)
data_JRA = xr.open_dataset("/home/b08209006/IONTU/BSF/JRA_msftbarot/msftbarot_Omon_TaiESM1"
                           "-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc", decode_times=False)

BSF_IAF = np.asarray(data_IAF['msftbarot'][120:])
BSF_JRA = np.asarray(data_JRA['msftbarot'][:-108])
lon = np.asarray(data_IAF['nlon'])
lat = np.asarray(data_IAF['nlat'])

BSF_IAF_all_mean, BSF_JRA_all_mean = np.average(BSF_IAF, axis=0) / 10 ** 9, np.average(BSF_JRA, axis=0) / 10 ** 9

# plot IAF
plt.tight_layout()
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.add_feature(cfeature.LAND)

ax.contourf(lon, lat, BSF_IAF_all_mean, cmap=cm.rainbow, transform=ccrs.PlateCarree(),
            levels=np.arange(-90, 250 + 10, 10))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.rainbow), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-90, 250 + 10, 10))
cbar.set_ticks([-80, -40, 0, 40, 80, 120, 160, 200, 240])

cn1 = ax.contour(lon, lat, BSF_IAF_all_mean, transform=ccrs.PlateCarree(), colors='k', levels=np.arange(-90, 250+20, 20))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.show()

# plot JRA
plt.tight_layout()
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.add_feature(cfeature.LAND)

ax.contourf(lon, lat, BSF_JRA_all_mean, cmap=cm.rainbow, transform=ccrs.PlateCarree(),
            levels=np.arange(-90, 250 + 10, 10))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.rainbow), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-90, 250 + 10, 10))
cbar.set_ticks([-80, -40, 0, 40, 80, 120, 160, 200, 240])

cn1 = ax.contour(lon, lat, BSF_JRA_all_mean, transform=ccrs.PlateCarree(), colors='k', levels=np.arange(-90, 250+20, 20))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.show()

# plot JRA - IAF
bias = BSF_JRA_all_mean - BSF_IAF_all_mean
bias = np.where(bias > 30, 30, bias)
bias = np.where(bias < -30, -30, bias)
plt.tight_layout()
plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.add_feature(cfeature.LAND)

ax.contourf(lon, lat, bias, cmap=cm.RdBu_r, transform=ccrs.PlateCarree(),
            levels=np.arange(-30, 30 + 5, 5))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-30, 30 + 5, 5))
cbar.set_ticks(np.arange(-25, 25+10, 10))

cn1 = ax.contour(lon, lat, bias, transform=ccrs.PlateCarree(), colors='k', levels=np.arange(-30, 30 + 10, 10))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.show()

