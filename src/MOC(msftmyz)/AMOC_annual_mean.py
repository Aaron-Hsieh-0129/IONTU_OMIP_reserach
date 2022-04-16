import numpy as np
import xarray as xr
import matplotlib.pyplot as plt


def Annual_mean(AMOC, years):
    AMOC_annual_mean = np.zeros([years])
    for i in range(years):
        AMOC_annual_mean[i] = sum(AMOC[i * 12:(i + 1) * 12]) / 12
    return AMOC_annual_mean


data_JRA = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/JRA_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gr_030601-036612.nc")
data_IAF = xr.open_dataset("/home/b08209006/IONTU/MOC("
                           "msftmyz)/IAF_msftmz/msftmz_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gr_031101-037212.nc")
data_OBS = xr.open_dataset("/home/b08209006/IONTU/MOC(msftmyz)/moc_transports.nc")

AMOC_JRA_glo = np.asarray(data_JRA['msftmz'][:, 0, :, 116])  # 26.5 N (202)
AMOC_IAF_glo = np.asarray(data_IAF['msftmz'][:, 0, :, 116])  # 26.5 N (202)

AMOC_JRA_max = np.zeros(732)
AMOC_IAF_max = np.zeros(744)
for i in range(732):
    AMOC_JRA_max[i] = np.nanmax(AMOC_JRA_glo[i])

for i in range(744):
    AMOC_IAF_max[i] = np.nanmax(AMOC_IAF_glo[i])

year_JRA = 61
year_IAF = 62
AMOC_JRA_annual_mean = Annual_mean(AMOC_JRA_max, year_JRA)
AMOC_IAF_annual_mean = Annual_mean(AMOC_IAF_max, year_IAF)

AMOC_OBS = np.asarray(data_OBS["moc_mar_hc10"][548:9314])  # 2005~2017
AMOC_OBS_max = np.zeros(8766)
for i in range(8766):
    AMOC_OBS_max[i] = np.nanmax(AMOC_OBS[i])


AMOC_2005 = np.average(AMOC_OBS_max[0:730])
AMOC_2006 = np.average(AMOC_OBS_max[730:1460])
AMOC_2007 = np.average(AMOC_OBS_max[1460:2190])
AMOC_2008 = np.average(AMOC_OBS_max[2190:2922])
AMOC_2009 = np.average(AMOC_OBS_max[2922:3652])
AMOC_2010 = np.average(AMOC_OBS_max[3652:4382])
AMOC_2011 = np.average(AMOC_OBS_max[4382:5112])
AMOC_2012 = np.average(AMOC_OBS_max[5112:5844])
AMOC_2013 = np.average(AMOC_OBS_max[5844:6574])
AMOC_2014 = np.average(AMOC_OBS_max[6574:7304])
AMOC_2015 = np.average(AMOC_OBS_max[7304:8034])
AMOC_2016 = np.average(AMOC_OBS_max[8034:8766])
AMOC_OBS_annual_mean = np.asarray([AMOC_2005, AMOC_2006, AMOC_2007, AMOC_2008, AMOC_2009, AMOC_2010,
                                   AMOC_2011, AMOC_2012, AMOC_2013, AMOC_2014, AMOC_2015, AMOC_2016])

np.savetxt("AMOC_OBS_annual_mean.txt", AMOC_OBS_annual_mean)
np.savetxt("AMOC_IAF_annual_mean.txt", AMOC_IAF_annual_mean)
np.savetxt("AMOC_JRA_annual_mean.txt", AMOC_JRA_annual_mean)

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [Sv]")
plt.text(67, 21.5, "Unit: Sv", fontsize=12)
plt.plot(np.arange(0, 62, 1), AMOC_IAF_annual_mean, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), AMOC_JRA_annual_mean, lw=3, color='#FF0021')
plt.plot(np.arange(58, 70, 1), AMOC_OBS_annual_mean, lw=3, color='k')
plt.legend(['IAF', 'JRA', 'OBS'], loc="upper left")
plt.show()
