import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import xarray as xr
from mpl_toolkits.mplot3d import Axes3D

data_YRYM = xr.open_dataset("YRYM_Ernesto_ocean_his_d01.nc")
data_NRNM = xr.open_dataset("NRNM_Ernesto_ocean_his_d01.nc")
data_wolf = xr.open_dataset("postwrf.nc")
dust = np.asarray(data_wolf['QCLOUD'])

lon_wolf = np.asarray(data_wolf['lon'][0])
lat_wolf = np.asarray(data_wolf['lat'][0])
lon = np.asarray(data_YRYM['lon_rho'])
lat = np.asarray(data_YRYM['lat_rho'])

PH = np.asarray(data_wolf['PH'])
PHB = np.asarray(data_wolf['PHB'])
height = (PH + PHB) / 9.81
height_mean = np.mean(np.mean(height, axis=1), axis=1)

T_YRYM = np.asarray(data_YRYM['temp'][:, 24, :, :])
T_NRNM = np.asarray(data_NRNM['temp'][:, 24, :, :])
T_diff = T_NRNM - T_YRYM
T_diff = np.where(T_diff <= -3.5, -3.5, T_diff)
T_diff = np.where(T_diff >= 3.5, 3.5, T_diff)
# T_YRYM = np.where(T_YRYM > 10 ** 5, np.nan, T_YRYM)
# T_NRNM = np.where(T_NRNM > 10 ** 5, np.nan, T_NRNM)
T_diff = T_NRNM - T_YRYM

for i in range(240, 245, 1):
    fig = plt.figure()
    ax = fig.gca(projection="3d")

    ax.grid(False)
    ax.set_xticks([])  # 不显示x坐标轴
    ax.set_yticks([])  # 不显示y坐标轴
    ax.xaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
    ax.yaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
    ax.zaxis._axinfo["grid"]['color'] = (1, 1, 1, 0)
    ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
    ax.axes.get_xaxis().set_visible(False)
    ax.axes.get_yaxis().set_visible(False)
    ax.set_zticks([0, height_mean[15], height_mean[24], height_mean[36]])

    elev, azim = 17, -45
    ax.view_init(elev=elev, azim=azim)
    cset0 = ax.contourf3D(lon, lat, T_diff[i], zdir='z', offset=0, cmap=cm.RdBu_r,
                          levels=np.arange(-3.5, 3.5 + 0.05, 0.05))
    # plt.colorbar(cset0, orientation="horizontal")
    # cset1 = ax.contourf3D(lon_wolf, lat_wolf, dust[5], zdir='z', offset=height_mean[5], cmap=cm.coolwarm, alpha=0.7)
    cset2 = ax.contourf3D(lon_wolf, lat_wolf, dust[15], zdir='z', offset=height_mean[15], cmap=cm.coolwarm, alpha=0.3)
    cset3 = ax.contourf3D(lon_wolf, lat_wolf, dust[24], zdir='z', offset=height_mean[24], cmap=cm.coolwarm, alpha=0.3)
    cset4 = ax.contourf3D(lon_wolf, lat_wolf, dust[36], zdir='z', offset=height_mean[36], cmap=cm.coolwarm, alpha=0.3)

    ax.set_zlim(-1000, 18900)
    # plt.savefig("Dust_Wolf_%d.png" % i)
    plt.show()
    plt.close()
