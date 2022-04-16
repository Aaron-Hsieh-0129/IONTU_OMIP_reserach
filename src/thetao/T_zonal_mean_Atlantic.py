import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

data_GTIAF_QVOLa_cycle6 = xr.open_dataset("/home/b08209006/IONTU/thetao/IAF_thetao/thetao_Omon_TaiESM1"
                                          "-TIMCOM_omip2_311-372.nc")
data_GTJRA_QVOLa_cycle6 = xr.open_dataset("/home/b08209006/IONTU/MHT(hfbasin)/JRA_hfbasin/gn/hfbasin_Omon_TaiESM1"
                                          "-TIMCOM_omip2_306-366.nc")

lon_IAF = np.asarray(data_GTIAF_QVOLa_cycle6['nlon'])
lat_IAF = np.asarray(data_GTIAF_QVOLa_cycle6['nlat'])

lev_IAF = np.asarray(data_GTIAF_QVOLa_cycle6['lev'])

T_JRA = np.asarray(data_GTJRA_QVOLa_cycle6['thetao'][:, :, 202, :])
T_IAF = np.asarray(data_GTIAF_QVOLa_cycle6['thetao'][:, :, 202, :])
