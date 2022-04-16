import numpy as np
import matplotlib.pyplot as plt

SSTGA_cycle_GTIAF_QVOLa = np.loadtxt("SSTGA_cycle_GTIAF_QVOLa.txt")
SSTGA_cycle_GTJRA_QVOLa = np.loadtxt("SSTGA_cycle_GTJRA_QVOLa.txt")
SSTGA_observation = np.loadtxt("SSTGA_observation.txt")


plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
plt.ylim([17.8, 18.8])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Temperature [$\degree$C]")
plt.text(67, 18.725, "Unit: $\degree$C", fontsize=12)
plt.plot(np.arange(0, 62, 1), SSTGA_cycle_GTIAF_QVOLa[248:309+1], lw=3, color='#08FF1D')
plt.plot(np.arange(0, 62, 1), SSTGA_cycle_GTIAF_QVOLa[310:], lw=3, color='#0303FF', linestyle='--')
plt.plot(np.arange(10, 71, 1), SSTGA_cycle_GTJRA_QVOLa[305:], lw=3, color='#5AFCFF')
plt.plot(np.arange(10, 71, 1), SSTGA_cycle_GTJRA_QVOLa[244:305], lw=3, color='#FF0021', linestyle='--')
# plt.axhline(SSTGA_observation, color='k', lw=2)
plt.legend(['IAF_cycle5', 'IAF_cycle6', 'JRA_cycle5', 'JRA_cycle6'], ncol=2,
           loc="upper left")


plt.show()