import numpy as np
import matplotlib.pyplot as plt

SSSGA_cycle_GTIAF_QVOLa = np.loadtxt("SSSGA_cycle_GTIAF_QVOLa.txt")
SSSGA_cycle_GTJRA_QVOLa = np.loadtxt("SSSGA_cycle_GTJRA_QVOLa.txt")
SSSGA_observation = np.loadtxt("SSSGA_observation.txt")

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.ylim([34.2, 34.6])
plt.xticks([2, 12, 22, 32, 42, 52], ['1950', '1960', '1970', '1980', '1990', '2000'])
plt.ylabel("Salinity [psu]")
plt.text(66.5, 34.57, "Unit: psu", fontsize=12)
plt.plot(np.arange(0, 62, 1), SSSGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), SSSGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#FF0021')
# plt.axhline(SSSGA_observation, color='k', lw=3)
plt.legend(['IAF', 'JRA'], loc='upper left')

plt.show()
