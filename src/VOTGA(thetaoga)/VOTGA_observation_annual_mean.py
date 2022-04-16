import scipy.io as sio
import numpy as np
import netCDF4 as nc


def Annual_mean(vot):
    vot_annual_mean = np.sum(vot, axis=3) / 12
    return vot_annual_mean


data = nc.Dataset("/home/b08209006/IONTU/VOTGA(thetaoga)/volcello.nc")
volcello = np.asarray(data['volcello'])
volcello = volcello.swapaxes(2, 0)

data2 = sio.loadmat("levitus.mat")
VOT = data2['T'][:, :, :, :]

VOT_annual_mean = Annual_mean(VOT)
VOT_annual_mean = np.where(np.isnan(VOT_annual_mean), 0, VOT_annual_mean)
volcello = np.nan_to_num(VOT_annual_mean * volcello / VOT_annual_mean)
VOTGA_annual_mean = np.asarray([np.sum(VOT_annual_mean * volcello) / np.sum(volcello)])
np.savetxt("VOTGA_observation.txt", VOTGA_annual_mean)