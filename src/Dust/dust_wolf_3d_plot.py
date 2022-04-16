import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import xarray as xr

data_wolf = xr.open_dataset("Wolf_YRYM_dust.nc")
dust = np.asarray(data_wolf['DUST_1'][0])

lon_wolf = np.asarray(data_wolf['XLONG'][0])
lat_wolf = np.asarray(data_wolf['XLAT'][0])

PH = np.asarray(data_wolf['PH'][0])
PHB = np.asarray(data_wolf['PHB'][0])
height = (PH + PHB) / 9.81
height_mean = np.mean(np.mean(height, axis=1), axis=1)

# Dust_5 = plt.contourf(dust[5], cmap=cm.YlOrBr, levels=np.arange(0, 6.4 * 10 ** -9, 5 * 10 ** -11))
# Dust_11 = plt.contourf(dust[11], cmap=cm.YlOrBr, levels=np.arange(0, 5.6 * 10 ** -9, 5 * 10 ** -11))
# Dust_15 = plt.contourf(dust[15], cmap=cm.YlOrBr, levels=np.arange(0, 1.2 * 10 ** -9, 5 * 10 ** -11))
# Dust_36 = plt.contourf(dust[36], cmap=cm.YlOrBr, levels=np.arange(0, 4.7 * 10 ** -14, 5 * 10 ** -16))

fig = plt.figure()
ax = fig.gca(projection="3d")

ax.grid(False)
ax.set_xticks([])  # 不顯示x軸
ax.set_yticks([])  # 不顯示y軸
ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.set_zticks([height_mean[5], height_mean[15], height_mean[24], height_mean[36]])

elev, azim = 17, -45
ax.view_init(elev=elev, azim=azim)


cset1 = ax.contourf(lon_wolf, lat_wolf, dust[5], zdir='z', offset=height_mean[5], cmap=cm.coolwarm, alpha=0.7)
cset2 = ax.contourf(lon_wolf, lat_wolf, dust[15], zdir='z', offset=height_mean[15], cmap=cm.coolwarm, alpha=0.5)
cset3 = ax.contourf(lon_wolf, lat_wolf, dust[24], zdir='z', offset=height_mean[24], cmap=cm.coolwarm, alpha=0.4)
cset4 = ax.contourf(lon_wolf, lat_wolf, dust[36], zdir='z', offset=height_mean[36], cmap=cm.coolwarm, alpha=0.3)

# plt.colorbar(cset4)
# plt.colorbar(cset2)
# plt.colorbar(cset3)

ax.set_zlim(-1000, 18900)
plt.show()
