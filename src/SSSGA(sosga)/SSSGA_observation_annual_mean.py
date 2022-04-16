import scipy.io as sio
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def Annual_mean(sss):
    sss_annual_mean = np.sum(sss, axis=2) / 12
    return sss_annual_mean


data_vol = xr.open_dataset("volcello.nc")
areaGd = np.asarray(data_vol['volcello'][0]).swapaxes(0, 1)

data2 = sio.loadmat("levitus.mat")
SSS = data2['S'][:, :, 0, :]
SSS_annual_mean = Annual_mean(SSS)
SSS_annual_mean = np.where(np.isnan(SSS_annual_mean), 0, SSS_annual_mean)
areaGd = np.nan_to_num(SSS_annual_mean * areaGd / SSS_annual_mean)
SSSGA_annual_mean = np.asarray([np.sum(SSS_annual_mean * areaGd) / np.sum(areaGd)])
np.savetxt("SSSGA_observation.txt", SSSGA_annual_mean)
