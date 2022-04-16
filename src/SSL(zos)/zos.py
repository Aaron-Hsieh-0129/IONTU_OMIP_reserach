import numpy as np
import xarray as xr
import scipy.io as sio
import matplotlib.pyplot as plt


def Annual_mean(zos, years):
    zos_annual_mean = np.zeros([years])
    for i in range(years):
        zos_annual_mean[i] = sum(zos[i * 12:(i + 1) * 12]) / 12
    return zos_annual_mean


data_IAF = xr.open_dataset("/home/b08209006/IONTU/SSL("
                           "zos)/IAF_zos/gn/zos_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc",
                           decode_times=False)
data_JRA = xr.open_dataset("/home/b08209006/IONTU/SSL("
                           "zos)/JRA_zos/gn/zos_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc",
                           decode_times=False)

zos_IAF = np.asarray(data_IAF['zos'])
zos_JRA = np.asarray(data_JRA['zos'])

data = sio.loadmat("areaGd.mat")
areaGd = np.asarray(data['areaGd']).swapaxes(0, 1)

zos_IAF_weight_mean = np.asarray([zos_IAF[i] * areaGd for i in range(744)]) / np.sum(areaGd)

zos_IAF_weight_mean = np.nansum(np.nansum(zos_IAF * areaGd, axis=1), axis=1) / np.sum(areaGd)
zos_JRA_weight_mean = np.nansum(np.nansum(zos_JRA * areaGd, axis=1), axis=1) / np.sum(areaGd)

year_IAF = 62
year_JRA = 61
zos_IAF_annual_mean = Annual_mean(zos_IAF_weight_mean, year_IAF)
zos_JRA_annual_mean = Annual_mean(zos_JRA_weight_mean, year_JRA)


plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
# plt.ylim([17.8, 18.8])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Height [m]")
# plt.text(67, 18.725, "Unit: $\degree$C", fontsize=12)
plt.plot(np.arange(0, 62, 1), zos_IAF_annual_mean, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), zos_JRA_annual_mean, lw=3, color='#FF0021')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)'])
plt.show()