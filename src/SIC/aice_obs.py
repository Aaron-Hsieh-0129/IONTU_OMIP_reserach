import xarray as xr
import matplotlib.pyplot as plt
import numpy as np
import scipy.io as sio


def Annual_mean(aice, years):
    aice_annual_mean = np.zeros([years, 180, 360])
    for i in range(years):
        aice_annual_mean[i] = sum(aice[i * 12:(i + 1) * 12]) / 12
    return aice_annual_mean


data_obs = xr.open_dataset("/home/b08209006/IONTU/SIC/HadISST_ice.nc")
data_area = xr.open_dataset("/data2/OMIP/TaiESM1-TIMCOM/GTJRA_v1.0/Ofx/areacello/gr/areacello_Ofx_TaiESM1"
                            "-TIMCOM_omip2_r1i1p1f1_gr.nc")

sic = np.asarray(data_obs["sic"][936:1788])  # 1948~2018
sic_annual_mean = Annual_mean(sic, 71)


def Distance1(Lat_A, Lng_A, Lat_B, Lng_B):  # 第一種計算方法
    ra = 6378.140  # 赤道半徑
    rb = 6356.755  # 極半徑 （km）
    flatten = (ra - rb) / ra  # 地球偏率
    rad_lat_A = np.radians(Lat_A)
    rad_lng_A = np.radians(Lng_A)
    rad_lat_B = np.radians(Lat_B)
    rad_lng_B = np.radians(Lng_B)
    pA = np.arctan(rb / ra * np.tan(rad_lat_A))
    pB = np.arctan(rb / ra * np.tan(rad_lat_B))
    xx = np.arccos(np.sin(pA) * np.sin(pB) + np.cos(pA) * np.cos(pB) * np.cos(rad_lng_A - rad_lng_B))
    c1 = (np.sin(xx) - xx) * (np.sin(pA) + np.sin(pB)) ** 2 / np.cos(xx / 2) ** 2
    c2 = (np.sin(xx) + xx) * (np.sin(pA) - np.sin(pB)) ** 2 / np.sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance


x = np.linspace(0, 360, 361)
y = np.linspace(-90, 90, 181)

xx, yy = np.meshgrid(x, y)

Lat_A = yy[:-1, :]
Lng_A = xx[:-1, :]
Lat_B = yy[1:, :]
Lng_B = xx[1:, :]
dy = Distance1(Lat_A, Lng_A, Lat_B, Lng_B) * 1000
Lat_A = yy[:, :-1]
Lng_A = xx[:, :-1]
Lat_B = yy[:, 1:]
Lng_B = xx[:, 1:]
dx = Distance1(Lat_A, Lng_A, Lat_B, Lng_B) * 1000
area = dx[:-1, :] * dy[:, :-1]

sic_south_area = np.nansum(np.nansum(np.asarray([area[0:90, :] * sic_annual_mean[i, 0:90, :] for i in range(71)]), axis=1), axis=1) / 10**12
sic_north_area = np.nansum(np.nansum(np.asarray([area[90:, :] * sic_annual_mean[i, 90:, :] for i in range(71)]), axis=1), axis=1) / 10**12
np.savetxt("sic_obs_south.txt", sic_south_area)
np.savetxt("sic_obs_north.txt", sic_north_area)