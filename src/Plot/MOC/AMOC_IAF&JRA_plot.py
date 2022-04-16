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

xx_IAF, yy_IAF = np.meshgrid(lat_IAF[56:], lev_IAF)
# plot
plt.tight_layout()
fig, ax = plt.subplots(2, 1, figsize=(8, 10), dpi=500)
fig.subplots_adjust(left=0.104, bottom=0.038, right=0.877, top=0.965, hspace=0.126)

# plot contourf
ax[0].contourf(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
               levels=np.arange(-9, 20 + 0.25, 0.25))
cax = plt.axes([0.91, 0.043, 0.035, 0.921])  # left, bottom, ,length
cb = fig.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="vertical", extend='both',
                  boundaries=np.arange(-10, 30 + 0.5, 0.5), ax=ax.ravel().tolist(), cax=cax)
cb.ax.tick_params()

# plot contour
cs1 = ax[0].contour(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
ax[0].clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.sca(ax[0])
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[0].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[0].set_ylabel("Depth (km)")

xx_JRA, yy_JRA = np.meshgrid(lat_JRA[56:], lev_JRA)
ax[1].contourf(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
               levels=np.arange(-9, 20 + 0.25, 0.25))
cs1 = ax[1].contour(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
ax[1].clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.sca(ax[1])
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
ax[1].set_ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
ax[1].set_ylabel("Depth (km)")

plt.savefig("AMOC.png")
plt.show()
