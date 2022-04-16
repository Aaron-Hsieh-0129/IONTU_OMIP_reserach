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


data_IAF = xr.open_dataset("/home/b08209006/IONTU/SST("
                           "tos)/IAF_tos/gn/tos_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc", decode_times=False)
data_JRA = xr.open_dataset("/home/b08209006/IONTU/SST("
                           "tos)/JRA_tos/gn/tos_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc", decode_times=False)
data_levitus = sio.loadmat("levitus.mat")

lon_IAF = np.asarray(data_IAF['nlon'])
lat_IAF = np.asarray(data_IAF['nlat'])
lon_IAF, lat_IAF = np.meshgrid(lon_IAF, lat_IAF)

SST_IAF = np.asarray(data_IAF['tos'][120:])
SST_JRA = np.asarray(data_JRA['tos'][:-108])
SST_OBS = data_levitus['T'][:, :, 0, :]


SST_IAF_ave = np.average(SST_IAF, axis=0)
SST_JRA_ave = np.average(SST_JRA, axis=0)
SST_OBS_ave = np.average(SST_OBS, axis=2).swapaxes(0, 1)

SST_IAF_bias = SST_IAF_ave - SST_OBS_ave
#SST_IAF_bias[238, 241] = np.nan     # 內陸點 影響最大值
#SST_IAF_bias[230, 79] = np.nan      # 內陸點 影響最小值
SST_JRA_bias = SST_JRA_ave - SST_OBS_ave
#SST_JRA_bias[238, 241] = np.nan     # 內陸點 影響最大值
#SST_JRA_bias[230, 79] = np.nan      # 內陸點 影響最小值

RMSE_IAF = RMSE(SST_IAF_ave, SST_OBS_ave)
RMSE_JRA = RMSE(SST_JRA_ave, SST_OBS_ave)

MEAN_IAF = np.nanmean(SST_IAF_bias)
MEAN_JRA = np.nanmean(SST_JRA_bias)

MAX_IAF = np.nanmax(SST_IAF_bias)
MAX_JRA = np.nanmax(SST_JRA_bias)

MIN_IAF = np.nanmin(SST_IAF_bias)
MIN_JRA = np.nanmin(SST_JRA_bias)

SST_IAF_bias_adjust = np.where(np.nan_to_num(SST_IAF_bias) >= 3, 3, SST_IAF_bias)
SST_IAF_bias_adjust = np.where(np.nan_to_num(SST_IAF_bias_adjust) <= -3, -3, SST_IAF_bias_adjust)
SST_JRA_bias_adjust = np.where(np.nan_to_num(SST_JRA_bias) >= 3, 3, SST_JRA_bias)
SST_JRA_bias_adjust = np.where(np.nan_to_num(SST_JRA_bias_adjust) <= -3, -3, SST_JRA_bias_adjust)

minLon = np.min(lon_IAF)
maxLon = np.max(lon_IAF)
minLat = np.min(lat_IAF)
maxLat = np.max(lat_IAF)

plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SST_IAF_bias_adjust, cmap=cm.RdBu_r, levels=np.arange(-3.5, 3.5 + 0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SST_IAF_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-3.6, 3.6 + 0.05, 0.05), pad=0.1, shrink=0.75, aspect=27)
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

# JRA
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SST_JRA_bias_adjust, cmap=cm.RdBu_r, levels=np.arange(-3.5, 3.5 + 0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SST_JRA_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-3.6, 3.6 + 0.05, 0.05), pad=0.1, shrink=0.75, aspect=27)
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

# OBS
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([-179.4375, 179.4375, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.LAND)
cn = ax.contourf(lon_IAF, lat_IAF, SST_OBS_ave, cmap=cm.jet, levels=np.arange(-4, 32 + 0.5, 0.5))
cn1 = ax.contour(lon_IAF, lat_IAF, SST_OBS_ave, colors='k')
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.jet), orientation="horizontal", extend='both',
             spacing='uniform', boundaries=np.arange(-4, 32 + 0.5, 0.5), pad=0.1, shrink=0.75, aspect=27)
# ax.set_title("RMSE = %.3f, MEAN = %.3f, MAX = %.3f, MIN = %.3f"
#             % (RMSE_GTJRA_QVOLa, MEAN_GTJRA_QVOLa, MAX_GTJRA_QVOLa, MIN_GTJRA_QVOLa), fontsize=15)
# 設定刻度
ax.set_xticks(np.arange(-180, 180 + 60, 60), crs=ccrs.PlateCarree())
ax.xaxis.set_minor_locator(plt.MultipleLocator(30))
ax.set_yticks(np.arange(-90, 90 + 30, 30), crs=ccrs.PlateCarree())
ax.yaxis.set_minor_locator(plt.MultipleLocator(15))
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())

plt.show()

# JRA - IAF
SST_JRA_IAF_bias = SST_JRA_ave - SST_IAF_ave
SST_JRA_IAF_bias_adjust = np.where(SST_JRA_IAF_bias <= -3, -3, SST_JRA_IAF_bias)
plt.tight_layout()
fig, ax = plt.subplots(figsize=(15, 8), subplot_kw={'projection': ccrs.PlateCarree()})
ax.set_extent([minLon, maxLon, minLat, maxLat], crs=ccrs.PlateCarree())
ax.coastlines(resolution='110m')
ax.grid(linestyle='--')
ax.add_feature(cfeature.BORDERS)
cn = ax.contourf(lon_IAF, lat_IAF, SST_JRA_IAF_bias_adjust, cmap=cm.RdBu_r, levels=np.arange(-3, 3 + 0.05, 0.05))
cn1 = ax.contour(lon_IAF, lat_IAF, SST_JRA_IAF_bias, colors='k')
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
