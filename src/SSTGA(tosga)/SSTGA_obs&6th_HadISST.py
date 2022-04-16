import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def Annual_mean(sst, years):
    sstga_annual_mean = np.zeros(years)
    for i in range(years):
        sstga_annual_mean[i] = sum(sst[i * 12:(i + 1) * 12]) / 12
    return sstga_annual_mean


data_Hadi = xr.open_dataset("/home/b08209006/IONTU/SSTGA(tosga)/HadISST_sst.nc")
SST_Hadi = np.asarray(data_Hadi['sst'])
SST_Hadi = np.where(SST_Hadi == -1000, np.nan, SST_Hadi)
data_area = xr.open_dataset("/home/b08209006/IONTU/SSTGA(tosga)/areacello_Ofx_TaiESM1-TIMCOM_omip2_r1i1p1f1_gr.nc")
areaGd = np.asarray(data_area["areacello"])
SSTGA_annual_mean = np.zeros(1805)
for i in range(1805):
    areaGd = (SST_Hadi[i] * areaGd) / SST_Hadi[i]
    SSTGA_annual_mean[i] = np.nansum(SST_Hadi[i] * areaGd) / np.nansum(areaGd)

SSTGA_annual_mean = SSTGA_annual_mean[:-5]
SSTGA_annual_mean = Annual_mean(SSTGA_annual_mean, 150)     # 1870~2018

np.savetxt("SSTGA_obs_HadISST.txt", SSTGA_annual_mean)

