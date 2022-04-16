import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cartopy.crs as ccrs
import cartopy.feature as cfeature

data_wolf = xr.open_dataset("/home/b08209006/IONTU/Dust/postwrf.nc")
data_YRYM = xr.open_dataset("/home/b08209006/IONTU/Dust/YRYM_Ernesto_ocean_his_d01.nc")
data_NRNM = xr.open_dataset("/home/b08209006/IONTU/Dust/NRNM_Ernesto_ocean_his_d01.nc")

lon = np.asarray(data_YRYM['lon_psi'][:, :])
lat = np.asarray(data_YRYM['lat_psi'][:, :])

# height
PH = np.asarray(data_wolf['PH'])
PHB = np.asarray(data_wolf['PHB'])
height = (PH + PHB) / 9.81
height_mean = np.mean(np.mean(height, axis=1), axis=1)

# zeta
zeta_YRYM = np.asarray(data_YRYM['zeta'][60:])

# u, v
u_YRYM = np.asarray(data_YRYM['u'][60:, 24, 1:, :])  # from 2015070100~2015100100
v_YRYM = np.asarray(data_YRYM['v'][60:, 24, :, 1:])

# QCLOUD
QCLOUD = np.asarray(data_wolf['QCLOUD'])

# TAUTOT8
TAUTOT8 = np.asarray(data_wolf)

fig = plt.figure(dpi=500)
ax = fig.gca(projection="3d")

ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zlim(0, 18900)
ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
# ax.axes.get_xaxis().set_visible(False)
# ax.axes.get_yaxis().set_visible(False)
ax.set_zticks([0, height_mean[15], height_mean[24], height_mean[36]])

elev, azim = 17, 315
ax.view_init(elev=elev, azim=azim)

# zeta_plot
zeta_plot = ax.contourf(lon, lat, zeta_YRYM[0, 1:, 1:], zdir='z', offset=0, cmap=cm.coolwarm)
plt.colorbar(zeta_plot, orientation="vertical", pad=0.1, shrink=0.75, aspect=27)

# u, v plot
# ax.quiver(lon[::10, ::10], lat[::10, ::10], 0, u_YRYM[0, ::10, ::10], v_YRYM[0, ::10, ::10], 0,
#          length=0.1, normalize=True, arrow_length_ratio=0.5)

# QCLOUD plot
# fig = plt.figure(dpi=500)
# ax = fig.gca(projection="3d")
# ax.contourf(lon, lat, QCLOUD[0, 0, 1:-1, 1:-1])

plt.show()
