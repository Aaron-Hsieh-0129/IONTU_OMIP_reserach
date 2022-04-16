import numpy as np
import matplotlib.pyplot as plt

VOSGA_cycle_GTIAF_QVOLa = np.loadtxt("VOSGA_cycle_GTIAF_QVOLa.txt")
VOSGA_cycle_GTJRA_QVOLa = np.loadtxt("VOSGA_cycle_GTJRA_QVOLa.txt")
VOSGA_observation = np.loadtxt("VOSGA_observation.txt")

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 372])
plt.ylim([34.7115, 34.715])
plt.ylabel("Salinity [psu]")
plt.text(350, 34.7147, "Unit: psu", fontsize=12)
plt.plot(VOSGA_cycle_GTIAF_QVOLa, lw=3, color='#0303FF')
plt.plot(VOSGA_cycle_GTJRA_QVOLa, lw=3, color='#FF0021')
# plt.axhline(VOSGA_observation, color='k', lw=3)
plt.legend(['IAF', 'JRA'], loc="upper left")
plt.yticks([34.7115, 34.7120, 34.7125, 34.7130, 34.7135, 34.7140, 34.7145, 34.7150],
           ["34.7115", "34.7120", "34.7125", "34.7130", "34.7135", "34.7140", "34.7145", "34.7150"])

plt.axvline(61, linestyle='--', color='#0EA830')
plt.axvline(62, linestyle='--', color='#FF04FA')
plt.axvline(122, linestyle='--', color='#0EA830')
plt.axvline(124, linestyle='--', color='#FF04FA')
plt.axvline(183, linestyle='--', color='#0EA830')
plt.axvline(186, linestyle='--', color='#FF04FA')
plt.axvline(244, linestyle='--', color='#0EA830')
plt.axvline(248, linestyle='--', color='#FF04FA')
plt.axvline(305, linestyle='--', color='#0EA830')
plt.axvline(310, linestyle='--', color='#FF04FA')
plt.show()