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

# Obs 2005~2009
data = xr.open_dataset("mocha_mht_data_ERA5_v2018_2.nc")
AMOC = np.flip(np.asarray(data["moc"][548:4199+1, :]))  # 2005~2009
depth = np.flip(np.asarray(data["z"]))

AMOC_RAPID_ave = np.average(AMOC, axis=0)

"""
# plot JRA Atlantic
plt.tight_layout()
ax = plt.contourf(AMOC_JRA_Atlantic_arctic_ave, cmap=cm.gist_rainbow, levels=np.arange(-9, 18 + 0.25, 0.5))
cs1 = plt.contour(AMOC_JRA_Atlantic_arctic_ave, colors='k')
plt.clabel(cs1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(ax, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_JRA_Atlantic_arctic_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

# plot JRA Indian
plt.tight_layout()
bx = plt.contourf(AMOC_JRA_Indian_Pacific_ave, cmap=cm.gist_rainbow, levels=np.arange(-60, 30 + 0.5, 1))
cs2 = plt.contour(AMOC_JRA_Indian_Pacific_ave, colors='k')
plt.clabel(cs2, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(bx, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_JRA_Indian_Pacific_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

# plot JRA global
plt.tight_layout()
cx = plt.contourf(AMOC_JRA_Global_ave, cmap=cm.gist_rainbow, levels=np.arange(-50, 40 + 0.5, 1))
cs3 = plt.contour(AMOC_JRA_Global_ave, colors='k')
plt.clabel(cs3, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(cx, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_JRA_Global_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

# plot IAF Atlantic
plt.tight_layout()
ax = plt.contourf(AMOC_IAF_Atlantic_arctic_ave, cmap=cm.gist_rainbow, levels=np.arange(-8, 20 + 0.5, 0.5))
cs1 = plt.contour(AMOC_IAF_Atlantic_arctic_ave, colors='k')
plt.clabel(cs1, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(ax, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_IAF_Atlantic_arctic_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

# plot IAF Indian
plt.tight_layout()
bx = plt.contourf(AMOC_IAF_Indian_Pacific_ave, cmap=cm.gist_rainbow, levels=np.arange(-75, 30 + 1, 1))
cs2 = plt.contour(AMOC_IAF_Indian_Pacific_ave, colors='k')
plt.clabel(cs2, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(bx, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_IAF_Indian_Pacific_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

# plot JRA global
plt.tight_layout()
cx = plt.contourf(AMOC_IAF_Global_ave, cmap=cm.gist_rainbow, levels=np.arange(-60, 45 + 1, 1))
cs3 = plt.contour(AMOC_IAF_Global_ave, colors='k')
plt.clabel(cs3, inline=1, fontsize=10, fmt="%1.1f")
plt.colorbar(cx, extend='both', extendfrac='auto')
plt.xticks(np.linspace(0, 287, 7), ["85.56$\degree$S", "53.26$\degree$S", "28.53$\degree$S",
                                    "8.21$\degree$S",
                                    "28.53$\degree$N", "53.26$\degree$N", "85.56$\degree$N"])
plt.ylim(44, 0)
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()

plt.tight_layout()
plt.ylim(44, 0)
plt.plot(AMOC_IAF_Global_ave[:, 202], np.linspace(0, 44, 45))
plt.yticks(np.linspace(0, 44, 6), ["0km", "1km", "2km", "3km", "4km", "5km"])
plt.show()
"""
# IAF
plt.figure(figsize=(8, 6))
xx_IAF, yy_IAF = np.meshgrid(lat_IAF[56:], lev_IAF)
plt.tight_layout()
ax = plt.contourf(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
                  levels=np.arange(-9, 20 + 0.25, 0.25))
cs1 = plt.contour(xx_IAF, yy_IAF, AMOC_IAF_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
plt.clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="vertical", extend='both',
             spacing='uniform', boundaries=np.arange(-9, 20 + 0.25, 0.25), pad=0.05, aspect=27)
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
plt.ylabel("Depth (km)")
plt.show()

# JRA
plt.figure(figsize=(10, 6))
xx_JRA, yy_JRA = np.meshgrid(lat_JRA[56:], lev_JRA)

plt.tight_layout()
ax = plt.contourf(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], cmap=cm.gist_rainbow_r,
                  levels=np.arange(-9, 20 + 0.25, 0.25))
cs1 = plt.contour(xx_JRA, yy_JRA, AMOC_JRA_Atlantic_arctic_ave[:, 56:], colors='k', levels=np.linspace(-9, 20, 15))
plt.clabel(cs1, inline=1, fontsize=11, fmt="%1.1f")
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.gist_rainbow_r), orientation="vertical", extend='both',
             spacing='uniform', boundaries=np.arange(-9, 20 + 0.25, 0.25), pad=0.05, aspect=27)
plt.xticks(np.linspace(-20, 80, 6),
           ["20$\degree$S", "0$\degree$", "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.ylim(5304, 0)
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
plt.ylabel("Depth (km)")
plt.show()

# plot vertical
MAX_JRA = np.nanmax(AMOC_JRA_Atlantic_arctic_ave[:, 116])
MAX_IAF = np.nanmax(AMOC_IAF_Atlantic_arctic_ave[:, 116])
MAX_RAPID = np.nanmax(AMOC_RAPID_ave)

STD_JRA = np.std(AMOC_JRA_Atlantic_arctic_ave[:, 116], ddof=1)
STD_IAF = np.std(AMOC_IAF_Atlantic_arctic_ave[:, 116], ddof=1)
STD_RAPID = np.std(AMOC_RAPID_ave, ddof=1)

plt.tight_layout()
plt.figure(figsize=(5.5, 8))
plt.text(8, 4000, "JRA: MAX=%.2f$\pm$%.2f Sv" % (MAX_JRA, STD_JRA), fontsize=13)
plt.text(8, 4500, "IAF:  MAX=%.2f$\pm$%.2f Sv" % (MAX_IAF, STD_IAF), fontsize=13)
plt.text(7, 5000, "RAPID: MAX=%.2f$\pm$%.2f Sv" % (MAX_RAPID, STD_RAPID), fontsize=13)
plt.ylim(6000, 0)
plt.plot(AMOC_IAF_Atlantic_arctic_ave[:, 116], lev_IAF)
plt.plot(AMOC_JRA_Atlantic_arctic_ave[:, 116], lev_JRA)
plt.plot(AMOC_RAPID_ave, depth, 'k')
plt.yticks([0, 1000, 2000, 3000, 4000, 5000], ["0", "1", "2", "3", "4", "5"])
plt.legend(['IAF', 'JRA', 'RAPID'], loc="lower right", fontsize=12)
plt.ylabel("Depth (km)")
plt.grid(linestyle='--')
plt.show()
