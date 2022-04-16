import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

IAF = xr.open_dataset("/home/b08209006/IONTU/MHT(hfbasin)/IAF_hfbasin/gn/hfbasin_Omon_TaiESM1"
                      "-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
JRA = xr.open_dataset("/home/b08209006/IONTU/MHT(hfbasin)/JRA_hfbasin/gn/hfbasin_Omon_TaiESM1"
                      "-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")


# IAF
AMHT_IAF = np.asarray(IAF['hfbasin'][:, 0, :])
lat_IAF = np.asarray(IAF['nlat'])
AMHT_IAF_ave = np.average(AMHT_IAF, axis=0)

# JRA
AMHT_JRA = np.asarray(JRA['hfbasin'][:, 0, :])
lat_JRA = np.asarray(JRA['nlat'])
AMHT_JRA_ave = np.average(AMHT_JRA, axis=0)


plt.plot(lat_IAF[71:], AMHT_IAF_ave[71:], lw=3, color='#0303FF')
plt.plot(lat_JRA[71:], AMHT_JRA_ave[71:], lw=3, color='#FF0021')
plt.xlabel("Latitude")
plt.ylabel("Meridional Heat Transport [PW]")
plt.grid(linestyle="--")
plt.xticks(np.linspace(-40, 80, 7),
           ["40$\degree$S", "20$\degree$S", "0$\degree$",
            "20$\degree$N", "40$\degree$N", "60$\degree$N", "80$\degree$N"])
plt.legend(["IAF", "JRA"], loc="upper left")
plt.text(72, 0.95, "Unit: PW", fontsize=12)
plt.show()

