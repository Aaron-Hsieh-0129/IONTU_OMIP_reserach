import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

# IAF
data_IAF = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/IAF_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gr_031101-037212.nc")
GMOC_IAF = np.asarray(data_IAF['msftmz'][:, 2, :, :])
lat_IAF = np.asarray(data_IAF['nlat'])
lev_IAF = np.asarray(data_IAF['lev'])

GMOC_IAF_ave = np.average(GMOC_IAF, axis=0)
GMOC_IAF_ave_mo = np.where(np.nan_to_num(GMOC_IAF_ave) > 28, 28, GMOC_IAF_ave)
GMOC_IAF_ave_mo = np.where(np.nan_to_num(GMOC_IAF_ave_mo) < -8, -8, GMOC_IAF_ave)

# JRA
data_JRA = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/JRA_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gr_030601-036612.nc")
GMOC_JRA = np.asarray(data_JRA['msftmz'][:, 2, :, :])
lat_JRA = np.asarray(data_JRA['nlat'])
lev_JRA = np.asarray(data_JRA['lev'])

GMOC_JRA_ave = np.average(GMOC_JRA, axis=0)
GMOC_JRA_ave_mo = np.where(np.nan_to_num(GMOC_JRA_ave) > 28, 28, GMOC_JRA_ave)
GMOC_JRA_ave_mo = np.where(np.nan_to_num(GMOC_JRA_ave_mo) < -8, -8, GMOC_JRA_ave)


# plot IAF
xx_IAF, yy_IAF = np.meshgrid(lat_IAF, lev_IAF)
plt.tight_layout()
ax = plt.contourf(xx_IAF, yy_IAF, GMOC_IAF_ave_mo[:, :], cmap=cm.gist_rainbow_r
                  , levels=np.arange(-10, 30 + 0.5, 0.5))
cs1 = plt.contour(xx_IAF, yy_IAF, GMOC_IAF_ave[:, :], colors='k', levels=np.linspace(-60, 45, 25))
plt.clabel(cs1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="vertical", extend='both',
             spacing='uniform', boundaries=np.arange(-10, 30 + 0.5, 0.5), pad=0.05, aspect=27)
plt.xticks(np.linspace(-80, 80, 9),
           ["80$\degree$S", "60$\degree$S", "40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
plt.ylabel("Depth (km)")
plt.show()

# plot JRA
xx_IAF, yy_IAF = np.meshgrid(lat_IAF, lev_IAF)
plt.tight_layout()
ax = plt.contourf(xx_IAF, yy_IAF, GMOC_JRA_ave_mo[:, :], cmap=cm.gist_rainbow_r
                  , levels=np.arange(-10, 30 + 0.5, 0.5))
cs1 = plt.contour(xx_IAF, yy_IAF, GMOC_JRA_ave[:, :], colors='k', levels=np.linspace(-60, 45, 25))
plt.clabel(cs1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="vertical", extend='both',
             spacing='uniform', boundaries=np.arange(-10, 30 + 0.5, 0.5), pad=0.05, aspect=27)
plt.xticks(np.linspace(-80, 80, 9),
           ["80$\degree$S", "60$\degree$S", "40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
plt.ylabel("Depth (km)")
plt.show()
