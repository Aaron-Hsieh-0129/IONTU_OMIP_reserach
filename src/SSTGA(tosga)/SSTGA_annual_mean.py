import matplotlib.pyplot as plt
import netCDF4 as nc
import numpy as np


def SST_read(filename):
    data = nc.Dataset(filename)
    sstga = data['tosga'][:]
    return sstga


def Annual_mean(sst, years):
    sstga_annual_mean = np.zeros(years)
    for i in range(years):
        sstga_annual_mean[i] = sum(sst[i * 12:(i + 1) * 12]) / 12
    return sstga_annual_mean


# GTIAF_QVOLa
year_IAF = 62
sstga1 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_000101-006212.nc")
sstga2 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_006301-012412.nc")
sstga3 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_012501-018612.nc")
sstga4 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_018701-024812.nc")
sstga5 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_024901-031012.nc")
sstga6 = SST_read("/data2/OMIP/TaiESM1-TIMCOM/GTIAF_v1.1/Omon/tosga/gn/tosga_Omon_TaiESM1"
                  "-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")

cycle1, cycle2, cycle3 = Annual_mean(sstga1, year_IAF), Annual_mean(sstga2, year_IAF), Annual_mean(sstga3, year_IAF)
cycle4, cycle5, cycle6 = Annual_mean(sstga4, year_IAF), Annual_mean(sstga5, year_IAF), Annual_mean(sstga6, year_IAF)
cycle_GTIAF_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 366])
plt.ylim([17.8, 18.8])
plt.plot(cycle_GTIAF_QVOLa, lw=2)
plt.ylabel("Temperature [$\degree$C]")
plt.text(4, 18.725, "Unit: $\degree$C", fontsize=12)

"""# GTJRA_QVOLa
year_JRA = 61
sstga1 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_001-061.nc")
sstga2 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_062-122.nc")
sstga3 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_123-183.nc")
sstga4 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_184-244.nc")
sstga5 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_245-305.nc")
sstga6 = SST_read("/home/b08209006/IONTU/SSTGA(tosga)/JRA_tosga/tosga_Omon_TaiESM1-TIMCOM_omip2_306-366.nc")

cycle1, cycle2, cycle3 = Annual_mean(sstga1, year_JRA), Annual_mean(sstga2, year_JRA), Annual_mean(sstga3, year_JRA)
cycle4, cycle5, cycle6 = Annual_mean(sstga4, year_JRA), Annual_mean(sstga5, year_JRA), Annual_mean(sstga6, year_JRA)
cycle_GTJRA_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.plot(cycle_GTJRA_QVOLa, lw=2)
plt.legend(['GTIAF_QVOLa', 'GTJRA_QVOLa'])

plt.axvline(61, linestyle='--', color='g')
plt.axvline(122, linestyle='--', color='g')
plt.axvline(183, linestyle='--', color='g')
plt.axvline(244, linestyle='--', color='g')
plt.axvline(305, linestyle='--', color='g')
plt.show()

# Output data
np.savetxt("SSTGA_cycle_GTIAF_QVOLa.txt", cycle_GTIAF_QVOLa)
np.savetxt("SSTGA_cycle_GTJRA_QVOLa.txt", cycle_GTJRA_QVOLa)"""
