import numpy as np
import xarray as xr
import scipy.io as sio
import matplotlib.pyplot as plt


def T_read(filename):
    data = xr.open_dataset(filename)
    t = data['thetao'][:]
    return t


def Annual_mean(var, years):
    varga_annual_mean = np.zeros([years, 45, 288, 320])
    for i in range(years):
        varga_annual_mean[i] = sum(var[i * 12:(i + 1) * 12]) / 12
    return varga_annual_mean


# IAF
year_IAF = 62
tga1 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_000101-006212.nc")
tga2 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_006301-012412.nc")
tga3 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_012501-018612.nc")
tga4 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_018701-024812.nc")
tga5 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_024901-031012.nc")
tga6 = T_read(
    "/home/b08209006/IONTU/thetao/IAF_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
cycle1, cycle2, cycle3 = Annual_mean(tga1, year_IAF), Annual_mean(tga2, year_IAF), Annual_mean(tga3, year_IAF)
cycle4, cycle5, cycle6 = Annual_mean(tga4, year_IAF), Annual_mean(tga5, year_IAF), Annual_mean(tga6, year_IAF)
cycle_IAF = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()


# JRA
year_JRA = 61
tga1 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_000101-006112.nc")
tga2 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_006201-012212.nc")
tga3 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_012301-018312.nc")
tga4 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_018401-024412.nc")
tga5 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_024501-030512.nc")
tga6 = T_read(
    "/home/b08209006/IONTU/thetao/JRA_thetao/gn/thetao_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")
cycle1, cycle2, cycle3 = Annual_mean(tga1, year_JRA), Annual_mean(tga2, year_JRA), Annual_mean(tga3, year_JRA)
cycle4, cycle5, cycle6 = Annual_mean(tga4, year_JRA), Annual_mean(tga5, year_JRA), Annual_mean(tga6, year_JRA)
cycle_JRA = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()
