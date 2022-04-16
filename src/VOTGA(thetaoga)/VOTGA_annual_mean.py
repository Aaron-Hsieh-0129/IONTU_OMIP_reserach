import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt


def thetao_read(filename):
    data = nc.Dataset(filename)
    thetao = np.asarray(data['thetaoga'])
    return thetao


def Annual_mean(thetao, years):
    thetaoga_annual_mean = np.zeros(years)
    for i in range(years):
        thetaoga_annual_mean[i] = sum(thetao[i * 12:(i + 1) * 12]) / 12
    return thetaoga_annual_mean


# GTIAF
year_IAF = 62
thetaoga1 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_001"
                        "-062.nc")
thetaoga2 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_063"
                        "-124.nc")
thetaoga3 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_125"
                        "-186.nc")
thetaoga4 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_187"
                        "-248.nc")
thetaoga5 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_249"
                        "-310.nc")
thetaoga6 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/IAF_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_311"
                        "-372.nc")

cycle1, cycle2, cycle3 = Annual_mean(thetaoga1, year_IAF), Annual_mean(thetaoga2, year_IAF), Annual_mean(thetaoga3,
                                                                                                         year_IAF)
cycle4, cycle5, cycle6 = Annual_mean(thetaoga4, year_IAF), Annual_mean(thetaoga5, year_IAF), Annual_mean(thetaoga6,
                                                                                                         year_IAF)
cycle_GTIAF_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 366])
#plt.ylim([3.5, 4.1])
plt.plot(cycle_GTIAF_QVOLa, lw=2)
plt.ylabel("Temperature [$\degree$C]")
#plt.text(4, 18.725, "Unit: $\degree$C", fontsize=12)

# GTJRA_QVOLa
year_JRA = 61
thetaoga1 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_001"
                        "-061.nc")
thetaoga2 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_062"
                        "-122.nc")
thetaoga3 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_123"
                        "-183.nc")
thetaoga4 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_184"
                        "-244.nc")
thetaoga5 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_245"
                        "-305.nc")
thetaoga6 = thetao_read("/home/b08209006/IONTU/VOTGA(thetaoga)/JRA_thetaoga/thetaoga_Omon_TaiESM1-TIMCOM_omip2_306"
                        "-366.nc")

cycle1, cycle2, cycle3 = Annual_mean(thetaoga1, year_JRA), Annual_mean(thetaoga2, year_JRA), Annual_mean(thetaoga3,
                                                                                                         year_JRA)
cycle4, cycle5, cycle6 = Annual_mean(thetaoga4, year_JRA), Annual_mean(thetaoga5, year_JRA), Annual_mean(thetaoga6,
                                                                                                         year_JRA)
cycle_GTJRA_QVOLa = np.asarray([cycle1, cycle2, cycle3, cycle4, cycle5, cycle6]).flatten()

plt.plot(cycle_GTJRA_QVOLa, lw=2)
plt.legend(['GTIAF_QVOLa', 'GTJRA_QVOLa'])

plt.axvline(61, linestyle='--', color='g')
plt.axvline(122, linestyle='--', color='g')
plt.axvline(183, linestyle='--', color='g')
plt.axvline(244, linestyle='--', color='g')
plt.axvline(305, linestyle='--', color='g')
plt.show()

np.savetxt("VOTGA_cycle_GTIAF_QVOLa.txt", cycle_GTIAF_QVOLa)
np.savetxt("VOTGA_cycle_GTJRA_QVOLa.txt", cycle_GTJRA_QVOLa)
