import numpy as np
import matplotlib.pyplot as plt

VOTGA_cycle_GTIAF_QVOLa = np.loadtxt("VOTGA_cycle_GTIAF_QVOLa.txt")
VOTGA_cycle_GTJRA_QVOLa = np.loadtxt("VOTGA_cycle_GTJRA_QVOLa.txt")
VOTGA_observation = np.loadtxt("VOTGA_observation.txt")

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.ylim([4, 4.18])
plt.xticks([2, 12, 22, 32, 42, 52], ['1950', '1960', '1970', '1980', '1990', '2000'])
plt.ylabel("Temperature [$\degree$C]")
plt.text(67, 4.165, "Unit: $\degree$C", fontsize=12)
plt.plot(np.arange(0, 62, 1), VOTGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), VOTGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#FF0021')
# plt.axhline(VOTGA_observation, color='k', lw=3)
plt.legend(['IAF', 'JRA'], loc='upper left')

plt.show()
