import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
print(123123)

def soga_read(filename):
    data = nc.Dataset(filename)
    soga = np.asarray(data['soga'])
    return soga


def Annual_mean(so, years):
    soga_annual_mean = np.zeros(years)
    for i in range(years):
        soga_annual_mean[i] = sum(so[i * 12:(i + 1) * 12]) / 12
    return soga_annual_mean


# GTIAF
year_IAF = 62
vosga1 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_001-062.nc")
vosga2 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_063-124.nc")
vosga3 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_125-186.nc")
vosga4 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_187-248.nc")
vosga5 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_249-310.nc")
vosga6 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/IAF_soga/soga_Omon_TaiESM1-TIMCOM_omip2_311-372.nc")

cycle1, cycle2, cycle3 = Annual_mean(vosga1, year_IAF), Annual_mean(vosga2, year_IAF), Annual_mean(vosga3, year_IAF)
cycle4, cycle5, cycle6 = Annual_mean(vosga4, year_IAF), Annual_mean(vosga5, year_IAF), Annual_mean(vosga6, year_IAF)
cycle_GTIAF_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()


plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 366])
#plt.ylim([34.71, 34.715])
plt.plot(cycle_GTIAF_QVOLa, lw=2)
plt.ylabel("Salinity [psu]")
#plt.text(4, 34.46, "Unit: psu", fontsize=12)
print(123)

# GTJRA_QVOLa
year_JRA = 61
vosga1 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_001-061.nc")
vosga2 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_062-122.nc")
vosga3 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_123-183.nc")
vosga4 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_184-244.nc")
vosga5 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_245-305.nc")
vosga6 = soga_read("/home/b08209006/IONTU/VOSGA(soga)/JRA_soga/soga_Omon_TaiESM1-TIMCOM_omip2_306-366.nc")

cycle1, cycle2, cycle3 = Annual_mean(vosga1, year_JRA), Annual_mean(vosga2, year_JRA), Annual_mean(vosga3, year_JRA)
cycle4, cycle5, cycle6 = Annual_mean(vosga4, year_JRA), Annual_mean(vosga5, year_JRA), Annual_mean(vosga6, year_JRA)
cycle_GTJRA_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.plot(cycle_GTJRA_QVOLa, lw=2)
plt.legend(['GTIAF_QVOLa', 'GTJRA_QVOLa'])

plt.axvline(61, linestyle='--', color='g')
plt.axvline(122, linestyle='--', color='g')
plt.axvline(183, linestyle='--', color='g')
plt.axvline(244, linestyle='--', color='g')
plt.axvline(305, linestyle='--', color='g')
plt.tight_layout()
plt.show()

np.savetxt("VOSGA_cycle_GTIAF_QVOLa.txt", cycle_GTIAF_QVOLa)
np.savetxt("VOSGA_cycle_GTJRA_QVOLa.txt", cycle_GTJRA_QVOLa)
