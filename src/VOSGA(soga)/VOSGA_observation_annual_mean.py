import scipy.io as sio
import numpy as np
import netCDF4 as nc


def Annual_mean(vos):
    vos_annual_mean = np.sum(vos, axis=3) / 12
    return vos_annual_mean


data = nc.Dataset("/home/b08209006/IONTU/VOSGA(soga)/volcello.nc")
volcello = np.asarray(data['volcello'])
volcello = volcello.swapaxes(2, 0)

data2 = sio.loadmat("levitus.mat")
VOS = data2['S'][:, :, :, :]

VOS_annual_mean = Annual_mean(VOS)
VOS_annual_mean = np.where(np.isnan(VOS_annual_mean), 0, VOS_annual_mean)
volcello = np.nan_to_num(VOS_annual_mean * volcello / VOS_annual_mean)
VOSGA_annual_mean = np.asarray([np.sum(VOS_annual_mean * volcello) / np.sum(volcello)])
np.savetxt("VOSGA_observation.txt", VOSGA_annual_mean)