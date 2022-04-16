import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio


def Annual_mean(aice, years):
    aice_annual_mean = np.zeros([years, 288, 320])
    for i in range(years):
        aice_annual_mean[i] = sum(aice[i * 12:(i + 1) * 12]) / 12
    return aice_annual_mean


data_area = sio.loadmat("areaGd.mat")
areaGd = np.asarray(data_area['areaGd']).swapaxes(0, 1)

data_IAF = xr.open_dataset("aice_omip2_yht_GTIAF_QVOLa.nc")
aice_IAF = np.asarray(data_IAF['aice'])

data_JRA = xr.open_dataset("aice_omip2_yht_GTJRA_QVOLa.nc")
aice_JRA = np.asarray(data_JRA['aice'])

year_IAF = 372
aice_IAF = Annual_mean(aice_IAF, year_IAF)
aice_IAF /= 100
aice_IAF_area_array = aice_IAF * areaGd
aice_IAF_area = np.nansum(np.nansum(aice_IAF_area_array, axis=1), axis=1)

aice_IAF_weight_mean_north_hemi = aice_IAF_area_array[:, 0:144, :]
aice_IAF_area_north_hemi = np.nansum(np.nansum(aice_IAF_weight_mean_north_hemi, axis=1), axis=1)

aice_IAF_weight_mean_south_hemi = aice_IAF_area_array[:, 144:, :]
aice_IAF_area_south_hemi = np.nansum(np.nansum(aice_IAF_weight_mean_south_hemi, axis=1), axis=1)

year_JRA = 366
aice_JRA = Annual_mean(aice_JRA, year_JRA)
aice_JRA /= 100
aice_JRA_area_array = aice_JRA * areaGd
aice_JRA_area = np.nansum(np.nansum(aice_JRA_area_array, axis=1), axis=1)

aice_JRA_weight_mean_north_hemi = aice_JRA_area_array[:, 0:144, :]
aice_JRA_area_north_hemi = np.nansum(np.nansum(aice_JRA_weight_mean_north_hemi, axis=1), axis=1)

aice_JRA_weight_mean_south_hemi = aice_JRA_area_array[:, 144:, :]
aice_JRA_area_south_hemi = np.nansum(np.nansum(aice_JRA_weight_mean_south_hemi, axis=1), axis=1)

np.savetxt("aice_cycle_GTIAF_QVOLa_n.txt", aice_IAF_area_north_hemi)
np.savetxt("aice_cycle_GTIAF_QVOLa_s.txt", aice_IAF_area_south_hemi)

np.savetxt("aice_cycle_GTJRA_QVOLa_n.txt", aice_JRA_area_north_hemi)
np.savetxt("aice_cycle_GTJRA_QVOLa_s.txt", aice_JRA_area_south_hemi)

plt.plot(aice_IAF_area)
plt.plot(aice_JRA_area)
plt.show()