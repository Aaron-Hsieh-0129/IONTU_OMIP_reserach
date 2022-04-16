import numpy as np
import matplotlib.pyplot as plt

SSTGA_cycle_GTIAF_QVOLa = np.loadtxt("SSTGA_cycle_GTIAF_QVOLa.txt")
SSTGA_cycle_GTJRA_QVOLa = np.loadtxt("SSTGA_cycle_GTJRA_QVOLa.txt")
SSTGA_observation = np.loadtxt("/home/b08209006/IONTU/SSTGA(tosga)/SSTGA_obs_HadISST.txt")

plt.tight_layout()
plt.figure(figsize=(13, 6))
plt.grid(linestyle='--')
plt.xlim(0, 149)
plt.ylim(16.2, 19.2)
plt.ylabel("Temperature [$\degree$C]")
plt.text(140, 19.05, "Unit: $\degree$C", fontsize=12)
plt.xticks(np.arange(0, 149 + 30, 30), ['1870', '1900', '1930', '1960', '1990', '2020'])
plt.plot(np.arange(0 + 79, 62 + 79, 1), SSTGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF')
plt.plot(np.arange(10 + 79, 71 + 79, 1), SSTGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#FF0021')
plt.plot(np.arange(0, 150, 1), SSTGA_observation, lw=3, color='k')  # 1870~2018
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)', 'OBS (1870~2018)'], loc="upper left")

plt.show()