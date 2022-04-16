import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np


def SSS_read(filename):
    data = nc.Dataset(filename)
    sosga = data['sosga'][:]
    return sosga


def Annual_mean(sss, years):
    sssga_annual_mean = np.zeros(years)
    for i in range(years):
        sssga_annual_mean[i] = sum(sss[i * 12: (i + 1) * 12]) / 12
    return sssga_annual_mean


# GTIAF_QVOLa
year_IAF = 62
sssga1 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_001-062.nc")
ssaga2 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_063-124.nc")
sssga3 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_125-186.nc")
sssga4 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_187-248.nc")
sssga5 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_249-310.nc")
sssga6 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/IAF_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_311-372.nc")

cycle1, cycle2, cycle3 = Annual_mean(sssga1, year_IAF), Annual_mean(ssaga2, year_IAF), Annual_mean(sssga3, year_IAF)
cycle4, cycle5, cycle6 = Annual_mean(sssga4, year_IAF), Annual_mean(sssga5, year_IAF), Annual_mean(sssga6, year_IAF)
cycle_GTIAF_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 366])
# plt.ylim([33.96, 34.5])
plt.plot(cycle_GTIAF_QVOLa, lw=2)
plt.ylabel("Salinity [psu]")
plt.text(4, 34.46, "Unit: psu", fontsize=12)

# GTJRA_QVOLa
year_JRA = 61
sssga1 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_001-061.nc")
ssaga2 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_062-122.nc")
sssga3 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_123-183.nc")
sssga4 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_184-244.nc")
sssga5 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_245-305.nc")
sssga6 = SSS_read("/home/b08209006/IONTU/SSSGA(sosga)/JRA_sosga/sosga_Omon_TaiESM1-TIMCOM_omip2_306-366.nc")

cycle1, cycle2, cycle3 = Annual_mean(sssga1, year_JRA), Annual_mean(ssaga2, year_JRA), Annual_mean(sssga3, year_JRA)
cycle4, cycle5, cycle6 = Annual_mean(sssga4, year_JRA), Annual_mean(sssga5, year_JRA), Annual_mean(sssga6, year_JRA)
cycle_GTJRA_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.plot(cycle_GTJRA_QVOLa, lw=2)
plt.legend(['GTIAF_QVOLa', 'GTJRA_QVOLa'])

plt.axvline(61, linestyle='--', color='g')
plt.axvline(122, linestyle='--', color='g')
plt.axvline(183, linestyle='--', color='g')
plt.axvline(244, linestyle='--', color='g')
plt.axvline(305, linestyle='--', color='g')
plt.show()

np.savetxt("SSSGA_cycle_GTIAF_QVOLa.txt", cycle_GTIAF_QVOLa)
np.savetxt("SSSGA_cycle_GTJRA_QVOLa.txt", cycle_GTJRA_QVOLa)
