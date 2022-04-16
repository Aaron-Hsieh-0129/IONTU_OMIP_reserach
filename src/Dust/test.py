import numpy as np
import matplotlib.pyplot as plt
import xarray as xr
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.cm as cm
import matplotlib as mpl


data_wolf = xr.open_dataset("/home/b08209006/IONTU/Dust/postwrf.nc")
data_YRYM = xr.open_dataset("/home/b08209006/IONTU/Dust/YRYM_Ernesto_ocean_his_d01.nc")

dust = np.asarray(data_wolf['QCLOUD'][:, :, 1:-1, 1:-1])
T = np.asarray(data_YRYM['temp'][60:, 24, 1:, 1:])
RAINNC = np.asarray(data_wolf['RAINNC'][:, 1:-1, 1:-1])

lon = np.asarray(data_YRYM['lon_psi'][:, :])
lat = np.asarray(data_YRYM['lat_psi'][:, :])

PH = np.asarray(data_wolf['PH'][:, 1:-1, 1:-1])
PHB = np.asarray(data_wolf['PHB'][:, 1:-1, 1:-1])
height = (PH + PHB) / 9.81
height_mean = np.mean(np.mean(height, axis=1), axis=1)

minLon = np.min(lon)
maxLon = np.max(lon)
minLat = np.min(lat)
maxLat = np.max(lat)


fig = plt.figure(figsize=(15, 10))
ax = fig.gca(projection="3d")

ax.grid(False)
ax.set_xticks(np.arange(-60, 30, 20))
ax.set_yticks(np.arange(-10, 40, 20))
ax.set_xlabel("Lon")
ax.set_ylabel("Lat")
# ax.set_zlabel("Height [m]")
ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_zticks([])
ax.set_title("Layer 1&2: QCLOUD / Layer 3: RAINNC / Layer 4: SST", fontsize=18)

elev, azim = 17, -45
ax.view_init(elev=elev, azim=azim)

Tset = ax.contourf(lon, lat, T[0], zdir='z', offset=0, cmap=cm.RdBu_r, levels=np.arange(15, 33+0.5, 0.5))
cset0 = ax.contourf(lon, lat, RAINNC[0], zdir='z', offset=400, cmap=cm.coolwarm, alpha=0.7)
cset1 = ax.contourf(lon, lat, dust[0, 5], zdir='z', offset=height_mean[5], cmap=cm.coolwarm, alpha=0.7)
cset2 = ax.contourf(lon, lat, dust[0, 7], zdir='z', offset=height_mean[7], cmap=cm.coolwarm, alpha=0.7)
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.01, shrink=0.9, aspect=27, boundaries=np.arange(15, 33+0.5, 0.5))
ax.set_zlim(0, 1500)
#plt.savefig("%d.png" % i)
plt.show()
plt.close()