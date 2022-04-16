import numpy as np
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

SSTGA_cycle_GTIAF_QVOLa = np.loadtxt("SSTGA_cycle_GTIAF_QVOLa.txt")
SSTGA_cycle_GTJRA_QVOLa = np.loadtxt("SSTGA_cycle_GTJRA_QVOLa.txt")
SSTGA_observation = np.loadtxt("/home/b08209006/IONTU/SSTGA(tosga)/SSTGA_obs_HadISST.txt")

aice_cycle_GTIAF_QVOLa_n = np.loadtxt("aice_cycle_GTIAF_QVOLa_n.txt")
aice_cycle_GTIAF_QVOLa_s = np.loadtxt("aice_cycle_GTIAF_QVOLa_s.txt")
aice_cycle_GTJRA_QVOLa_n = np.loadtxt("aice_cycle_GTJRA_QVOLa_n.txt")
aice_cycle_GTJRA_QVOLa_s = np.loadtxt("aice_cycle_GTJRA_QVOLa_s.txt")

AMOC_IAF_annual_mean = np.loadtxt("AMOC_IAF_annual_mean.txt")
AMOC_JRA_annual_mean = np.loadtxt("AMOC_JRA_annual_mean.txt")
AMOC_OBS_annual_mean = np.loadtxt("AMOC_OBS_annual_mean.txt")

sic_obs_north = np.loadtxt("/home/b08209006/IONTU/Plot/6th_cycle (SSTGA, SIC, SSL, AMOC)/sic_obs_north.txt")
sic_obs_south = np.loadtxt("/home/b08209006/IONTU/Plot/6th_cycle (SSTGA, SIC, SSL, AMOC)/sic_obs_south.txt")

plt.tight_layout()
fig, ax = plt.subplots(4, 1, figsize=(20, 15))
fig.subplots_adjust(hspace=0.3)

ax[0].grid(linestyle='--')
ax[0].set_xlim([0, 71])
ax[0].set_ylim([16.2, 19.2])
ax[0].set_ylabel("Temperature [$\degree$C]")
ax[0].text(67, 18.95, "Unit: $\degree$C", fontsize=12)
ax[0].plot(np.arange(0, 62, 1), SSTGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF')
ax[0].plot(np.arange(10, 71, 1), SSTGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#FF0021')
ax[0].plot(np.arange(0, 71, 1), SSTGA_observation[79:], lw=3, color='k')
ax[0].legend(['IAF (1948~2009)', 'JRA (1958~2018)', 'OBS (1948~2018)'], loc="upper left")
plt.sca(ax[0])
plt.xticks(np.arange(2, 71, 10), ["1950", "1960", "1970", "1980", "1990", "2000", "2010"])


plt.sca(ax[1])
plt.xlim([0, 71])
plt.grid('--')
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [km$^2$]")
plt.text(67, 11.6, "Unit: km$^2$", fontsize=12)
plt.plot(np.arange(0, 62, 1), aice_cycle_GTIAF_QVOLa_n[310:] / 10**12, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), aice_cycle_GTJRA_QVOLa_n[305:] / 10**12, lw=3, color='#FF0021')
plt.plot(np.arange(0, 71, 1), sic_obs_north, lw=3, color='k')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)', 'OBS (1948~2018)'], loc="upper left")


plt.sca(ax[2])
plt.xlim([0, 71])
plt.grid('--')
# plt.ylim([17.8, 18.8])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [km$^2$]")
plt.text(67, 11.2, "Unit: km$^2$", fontsize=12)
plt.plot(np.arange(0, 62, 1), aice_cycle_GTIAF_QVOLa_s[310:] / 10**12, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), aice_cycle_GTJRA_QVOLa_s[305:] / 10**12, lw=3, color='#FF0021')
plt.plot(np.arange(0, 71, 1), sic_obs_south, lw=3, color='k')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)', 'OBS (1948~2018)'], loc="upper left")


plt.sca(ax[3])
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [Sv]")
plt.text(67, 21.8, "Unit: Sv", fontsize=12)
plt.plot(np.arange(0, 62, 1), AMOC_IAF_annual_mean, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), AMOC_JRA_annual_mean, lw=3, color='#FF0021')
plt.plot(np.arange(58, 70, 1), AMOC_OBS_annual_mean, lw=3, color='k')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)', 'OBS (1948~2018)'], loc="upper left")
plt.show()


