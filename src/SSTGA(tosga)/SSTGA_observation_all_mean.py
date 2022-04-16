import scipy.io as sio
import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def Annual_mean(sst):
    sst_annual_mean = np.sum(sst, axis=2) / 12
    return sst_annual_mean


data = sio.loadmat("areaGd.mat")
areaGd = data['areaGd']

data2 = sio.loadmat("levitus.mat")

SST = data2['T'][:, :, 0, :]
SST_annual_mean = Annual_mean(SST)
SST_annual_mean = np.where(np.isnan(SST_annual_mean), 0, SST_annual_mean)

areaGd = np.nan_to_num(SST_annual_mean * areaGd / SST_annual_mean)
SSTGA_annual_mean = np.asarray([np.sum(SST_annual_mean * areaGd) / np.sum(areaGd)])
np.savetxt("SSTGA_Observation.txt", SSTGA_annual_mean)

