import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

# IAF
data_IAF = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/IAF_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gr_031101-037212.nc")
AMOC_IAF = np.asarray(data_IAF['msftmz'])
lat_IAF = np.asarray(data_IAF['nlat'])
lev_IAF = np.asarray(data_IAF['lev'])

AMOC_IAF_Atlantic_arctic = AMOC_IAF[:, 0, :, :]
AMOC_IAF_Indian_Pacific = AMOC_IAF[:, 1, :, :]
AMOC_IAF_Global = AMOC_IAF[:, 2, :, :]

AMOC_IAF_Atlantic_arctic_ave = np.average(AMOC_IAF_Atlantic_arctic, axis=0)
AMOC_IAF_Indian_Pacific_ave = np.average(AMOC_IAF_Indian_Pacific, axis=0)
AMOC_IAF_Global_ave = np.average(AMOC_IAF_Global, axis=0)

# JRA
data_JRA = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/JRA_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gr_030601-036612.nc")
AMOC_JRA = np.asarray(data_JRA['msftmz'])
lat_JRA = np.asarray(data_JRA['nlat'])
lev_JRA = np.asarray(data_JRA['lev'])

AMOC_JRA_Atlantic_arctic = AMOC_JRA[:, 0, :, :]
AMOC_JRA_Indian_Pacific = AMOC_JRA[:, 1, :, :]
AMOC_JRA_Global = AMOC_JRA[:, 2, :, :]

AMOC_JRA_Atlantic_arctic_ave = np.average(AMOC_JRA_Atlantic_arctic, axis=0)
AMOC_JRA_Indian_Pacific_ave = np.average(AMOC_JRA_Indian_Pacific, axis=0)
AMOC_JRA_Global_ave = np.average(AMOC_JRA_Global, axis=0)

# IAF
GMOC_IAF = np.asarray(data_IAF['msftmz'][:, 2, :, :])

GMOC_IAF_ave = np.average(GMOC_IAF, axis=0)
GMOC_IAF_ave_mo = np.where(np.nan_to_num(GMOC_IAF_ave) > 28, 28, GMOC_IAF_ave)
GMOC_IAF_ave_mo = np.where(np.nan_to_num(GMOC_IAF_ave_mo) < -8, -8, GMOC_IAF_ave)

GMOC_JRA = np.asarray(data_JRA['msftmz'][:, 2, :, :])
GMOC_JRA_ave = np.average(GMOC_JRA, axis=0)
GMOC_JRA_ave_mo = np.where(np.nan_to_num(GMOC_JRA_ave) > 28, 28, GMOC_JRA_ave)
GMOC_JRA_ave_mo = np.where(np.nan_to_num(GMOC_JRA_ave_mo) < -8, -8, GMOC_JRA_ave)

# plot
plt.tight_layout()
fig, ax = plt.subplots(2, 2, figsize=(25, 20))
fig.subplots_adjust(top=0.98, bottom=0.128, left=0.042, right=0.977, hspace=0.211, wspace=0.129)
# AMOC_plot
xx_IAF, yy_IAF = np.meshgrid(lat_IAF[56:], lev_IAF)
# plot contourf
ax[0, 0].contourf(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
                  levels=np.arange(-9, 20 + 0.25, 0.25))

cax = fig.add_axes([0.043, 0.03, 0.94, 0.03])  # 1.距離左方 2.距離下方 3.長度 4.往上長度
cb = fig.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="horizontal", extend='both',
                  boundaries=np.arange(-10, 30 + 0.5, 0.5), ax=ax.ravel().tolist(), cax=cax)
cb.ax.tick_params()

# plot contour
cs1 = ax[0, 0].contour(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
ax[0, 0].clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.sca(ax[0, 0])
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[0, 0].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[0, 0].set_ylabel("Depth (km)")

xx_JRA, yy_JRA = np.meshgrid(lat_JRA[56:], lev_JRA)
ax[1, 0].contourf(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
                  levels=np.arange(-9, 20 + 0.25, 0.25))
cs1 = ax[1, 0].contour(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
ax[1, 0].clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.sca(ax[1, 0])
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[1, 0].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[1, 0].set_ylabel("Depth (km)")

# plot IAF
xx_IAF, yy_IAF = np.meshgrid(lat_IAF, lev_IAF)

# plot contourf
ax[0, 1].contourf(xx_IAF, yy_IAF, GMOC_IAF_ave_mo[:, :], cmap=cm.gist_rainbow_r
                  , levels=np.arange(-10, 30 + 0.5, 0.5))

# plot contour
cs1 = ax[0, 1].contour(xx_IAF, yy_IAF, GMOC_IAF_ave[:, :], colors='k', levels=np.linspace(-60, 45, 25))
ax[0, 1].clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.sca(ax[0, 1])
plt.xticks(np.linspace(-80, 80, 9),
           ["80$\degree$S", "60$\degree$S", "40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[0, 1].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[0, 1].set_ylabel("Depth (km)")

# plot JRA
xx_IAF, yy_IAF = np.meshgrid(lat_IAF, lev_IAF)
ax[1, 1].contourf(xx_IAF, yy_IAF, GMOC_JRA_ave_mo[:, :], cmap=cm.gist_rainbow_r
                  , levels=np.arange(-10, 30 + 0.5, 0.5))
cs1 = ax[1, 1].contour(xx_IAF, yy_IAF, GMOC_JRA_ave[:, :], colors='k', levels=np.linspace(-60, 45, 25))
ax[1, 1].clabel(cs1, inline=1, fontsize=10, fmt="%1.1f")
plt.sca(ax[1, 1])
plt.xticks(np.linspace(-80, 80, 9),
           ["80$\degree$S", "60$\degree$S", "40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[1, 1].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[1, 1].set_ylabel("Depth (km)")

plt.savefig("AMOC&GMOC.png")
plt.show()
