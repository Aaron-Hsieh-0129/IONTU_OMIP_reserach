import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
import cartopy.crs as ccrs
import matplotlib.cm as cm
import cartopy.feature as cfeature
import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

data_wolf = xr.open_dataset("/home/b08209006/IONTU/Dust/postwrf.nc")
data_YRYM = xr.open_dataset("/home/b08209006/IONTU/Dust/YRYM_Ernesto_ocean_his_d01.nc")

dust = np.asarray(data_wolf['TAUTOT8'])
T = np.asarray(data_YRYM['temp'][60:, 24, 1:, 1:])
RAINNC = np.asarray(data_wolf['RAINNC'][:, 1:-1, 1:-1])

lon = np.asarray(data_YRYM['lon_psi'][:, :])
lat = np.asarray(data_YRYM['lat_psi'][:, :])

PH = np.asarray(data_wolf['PH'][:, 1:, 1:])
PHB = np.asarray(data_wolf['PHB'][:, 1:, 1:])
height = (PH + PHB) / 9.81
height_mean = np.mean(np.mean(height, axis=1), axis=1)

minLon = np.min(lon)
maxLon = np.max(lon)
minLat = np.min(lat)
maxLat = np.max(lat)

fig = plt.figure()
ax = fig.add_subplot(projection="3d")

ax.set_xticks([])  # 不显示x坐标轴
ax.set_yticks([])  # 不显示y坐标轴
ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.axes.get_xaxis().set_visible(False)
ax.axes.get_yaxis().set_visible(False)

ax.add_feature(cfeature.LAND)
ax.set_xticks(np.linspace(-60, 30, 7), crs=ccrs.PlateCarree())
ax.set_yticks(np.arange(-10, 40 + 10, 10), crs=ccrs.PlateCarree())
ax.xaxis.set_major_formatter(LongitudeFormatter())
ax.yaxis.set_major_formatter(LatitudeFormatter())
# ax.set_zticks([0, height_mean[15], height_mean[24], height_mean[36]])
cset0 = ax.contourf3D(lon, lat, T[0], zdir='z', offset=0, cmap=cm.RdBu_r,
                      levels=np.arange(-3.5, 3.5 + 0.05, 0.05))

elev, azim = 17, -45
ax.view_init(elev=elev, azim=azim)

ax = plt.axes(projection=ccrs.PlateCarree())
ax.set_extent([minLon, maxLon, minLat, maxLat], crs=ccrs.PlateCarree())
axes1 = ax.contourf3D(lon, lat, T[0], zdir='z', offset=0, cmap=cm.RdYlBu_r, levels=np.arange(9, 33, 1))
ax.coastlines(resolution='110m')
plt.colorbar(axes1, orientation="horizontal", extend='both',
             spacing='uniform', pad=0.1, shrink=0.8, aspect=27)

axes2 = ax.contourf3D(lon, lat, RAINNC[0], zdir='z', offset=0, alpha=0.35, cmap=cm.RdBu_r)

# plt.savefig("%d.png" % i)
plt.show()
plt.close()


