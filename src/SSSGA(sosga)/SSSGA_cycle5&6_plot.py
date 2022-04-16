import numpy as np
import matplotlib.pyplot as plt

SSSGA_cycle_GTIAF_QVOLa = np.loadtxt("SSSGA_cycle_GTIAF_QVOLa.txt")
SSSGA_cycle_GTJRA_QVOLa = np.loadtxt("SSSGA_cycle_GTJRA_QVOLa.txt")
SSSGA_observation = np.loadtxt("SSSGA_observation.txt")

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.ylim([34.2, 34.7])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Salinity [psu]")
plt.text(66.5, 34.66, "Unit: psu", fontsize=12)
plt.plot(np.arange(0, 62, 1), SSSGA_cycle_GTIAF_QVOLa[248:310], lw=3, color='#08FF1D')
plt.plot(np.arange(0, 62, 1), SSSGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF', linestyle='--')
plt.plot(np.arange(10, 71, 1), SSSGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#5AFCFF')
plt.plot(np.arange(10, 71, 1), SSSGA_cycle_GTJRA_QVOLa[244:305], lw=3, color='#FF0021', linestyle='--')
# plt.axhline(SSSGA_observation, color='k', lw=2)
plt.legend(['IAF_cycle5', 'IAF_cycle6', 'JRA_cycle5', 'JRA_cycle6'], ncol=2, loc="upper left")

plt.show()
