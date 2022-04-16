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
                              "sos)/IAF_sos/gn/sos_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc", decode_times=False)
data_JRA_gn = xr.open_dataset("/home/b08209006/IONTU/SSS("
                              "sos)/JRA_sos/gn/sos_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc", decode_times=False)
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

RMSE_IAF = RMSE(SSS_IAF_ave, SSS_OBS_ave)
RMSE_JRA = RMSE(SSS_JRA_ave, SSS_OBS_ave)

MEAN_IAF = np.nanmean(SSS_IAF_bias)
MEAN_JRA = np.nanmean(SSS_JRA_bias)

MAX_IAF = np.nanmax(SSS_IAF_bias)
MAX_JRA = np.nanmax(SSS_JRA_bias)

MIN_IAF = np.nanmin(SSS_IAF_bias)
MIN_JRA = np.nanmin(SSS_JRA_bias)

SSS_IAF_bias_adjust = np.where(np.nan_to_num(SSS_IAF_bias) >= 1.8, 1.8, SSS_IAF_bias)
SSS_IAF_bias_adjust = np.where(np.nan_to_num(SSS_IAF_bias_adjust) <= -1.8, -1.8, SSS_IAF_bias_adjust)
SSS_JRA_bias_adjust = np.where(np.nan_to_num(SSS_JRA_bias) >= 1.8, 1.8, SSS_JRA_bias)
SSS_JRA_bias_adjust = np.where(np.nan_to_num(SSS_JRA_bias_adjust) <= -1.8, -1.8,
                               SSS_JRA_bias_adjust)

# IAF bias
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_IAF_bias_adjust, cmap=cm.RdBu_r, levels=np.arange(-1.8, 1.8+0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_IAF_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-1.8, 1.8 + 0.05, 0.05), pad=0.1, shrink=0.75, aspect=27)
ax.set_title("RMSE = %.3f, MEAN = %.3f, MAX = %.3f, MIN = %.3f"
             % (RMSE_IAF, MEAN_IAF, MAX_IAF, MIN_IAF), fontsize=15)
# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()

# JRA bias
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_JRA_bias_adjust,
                 cmap=cm.RdBu_r, levels=np.arange(-1.8, 1.8+0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_JRA_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-1.8, 1.8 + 0.05, 0.05), pad=0.1, shrink=0.75, aspect=27)
ax.set_title("RMSE = %.3f, MEAN = %.3f, MAX = %.3f, MIN = %.3f"
             % (RMSE_JRA, MEAN_JRA, MAX_JRA, MIN_JRA), fontsize=15)
# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()

# JRA - IAF
SSS_JRA_IAF_bias = SSS_JRA_ave - SSS_IAF_ave
SSS_JRA_IAF_bias_adjust = np.where(SSS_JRA_IAF_bias <= -3, -3, SSS_JRA_IAF_bias)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([minLon, maxLon, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SSS_JRA_IAF_bias_adjust, cmap=cm.RdBu_r, levels=np.arange(-3, 3 + 0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SSS_JRA_IAF_bias, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-3, 3 + 0.05, 0.05), pad=0.1, shrink=0.75, aspect=27)
# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()