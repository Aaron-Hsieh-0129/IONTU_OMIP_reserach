import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

IAF = xr.open_dataset("/home/b08209006/IONTU/MHT(hfbasin)/IAF_hfbasin/gn/hfbasin_Omon_TaiESM1"
                      "-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
JRA = xr.open_dataset("/home/b08209006/IONTU/MHT(hfbasin)/JRA_hfbasin/gn/hfbasin_Omon_TaiESM1"
                      "-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")


# IAF
GMHT_IAF = np.asarray(IAF['hfbasin'][:, 2, :])
lat_IAF = np.asarray(IAF['nlat'])
GMHT_IAF_ave = np.average(GMHT_IAF, axis=0)

# JRA
GMHT_JRA = np.asarray(JRA['hfbasin'][:, 2, :])
lat_JRA = np.asarray(JRA['nlat'])
GMHT_JRA_ave = np.average(GMHT_JRA, axis=0)


plt.plot(lat_IAF, GMHT_IAF_ave, lw=3, color='#0303FF')
plt.plot(lat_JRA, GMHT_JRA_ave, lw=3, color='#FF0021')
plt.xlabel("Latitude")
plt.ylabel("Meridional Heat Transport [PW]")
plt.grid(linestyle="--")
plt.xticks(np.linspace(-80, 80, 9),
           ["80$\degree$S", "60$\degree$S", "40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.legend(["IAF", "JRA"], loc="upper left")
plt.text(67, 1.3, "Unit: PW", fontsize=12)
plt.show()