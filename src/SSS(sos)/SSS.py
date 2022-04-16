import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl
import scipy.io as sio
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter


def RMSE(predictions, targets):
    return np.sqrt(np.nanmean((predictions - targets) ** 2))


def MEAN(predictions, targets):
    return np.nanmean(predictions - targets)


data_IAF_gn = xr.open_dataset("/home/b08209006/IONTU/SSS("
                              "sos)/IAF_sos/gn/sos_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
data_JRA_gn = xr.open_dataset("/home/b08209006/IONTU/SSS("
                              "sos)/JRA_sos/gn/sos_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")
data_levitus = sio.loadmat("levitus.mat")

lon_IAF = np.asarray(data_IAF_gn['nlon'])
lat_IAF = np.asarray(data_IAF_gn['nlat'])
minLon = np.max(lon_IAF)
maxLon = np.min(lon_IAF)
minLat = np.max(lat_IAF)
maxLat = np.min(lon_IAF)

SSS_IAF = np.asarray(data_IAF_gn['sos'][120:])
SSS_JRA = np.asarray(data_JRA_gn['sos'][:-108])
SSS_OBS = data_levitus['S'][:, :, 0, :]


SSS_IAF_ave = np.average(SSS_IAF, axis=0)
SSS_JRA_ave = np.average(SSS_JRA, axis=0)
SSS_OBS_ave = np.average(SSS_OBS, axis=2).swapaxes(0, 1)
SSS_IAF_bias = SSS_IAF_ave - SSS_OBS_ave
SSS_IAF_bias[251, 10] = np.nan
SSS_JRA_bias = SSS_JRA_ave - SSS_OBS_ave
SSS_JRA_bias[251, 10] = np.nan

SSS_IAF_ave = np.where(SSS_IAF_ave <= 24, 24, SSS_IAF_ave)
SSS_IAF_ave = np.where(SSS_IAF_ave >= 38, 38, SSS_IAF_ave)

SSS_JRA_ave = np.where(SSS_JRA_ave <= 24, 24, SSS_JRA_ave)
SSS_JRA_ave = np.where(SSS_JRA_ave >= 38, 38, SSS_JRA_ave)

SSS_OBS_ave = np.where(SSS_OBS_ave <= 24, 24, SSS_OBS_ave)
SSS_OBS_ave = np.where(SSS_OBS_ave >= 38, 38, SSS_OBS_ave)

# IAF
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_IAF_ave, cmap=cm.RdBu_r, levels=np.arange(24, 38+1, 1))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_IAF_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(24, 38+1, 1), pad=0.1, shrink=0.75, aspect=27)

# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()

# JRA
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_JRA_ave, cmap=cm.RdBu_r, levels=np.arange(24, 38+1, 1))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_JRA_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(24, 38+1, 1), pad=0.1, shrink=0.75, aspect=27)

# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
plt.show()

# OBS
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_OBS_ave, cmap=cm.RdBu_r, levels=np.arange(24, 38+1, 1))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_OBS_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(24, 38+1, 1), pad=0.1, shrink=0.75, aspect=27)

# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()
