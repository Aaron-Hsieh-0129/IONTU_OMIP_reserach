import numpy as np
import matplotlib.pyplot as plt

SSTGA_cycle_GTIAF_QVOLa = np.loadtxt("SSTGA_cycle_GTIAF_QVOLa.txt")
SSTGA_cycle_GTJRA_QVOLa = np.loadtxt("SSTGA_cycle_GTJRA_QVOLa.txt")
VOTGA_cycle_GTIAF_QVOLa = np.loadtxt("VOTGA_cycle_GTIAF_QVOLa.txt")
VOTGA_cycle_GTJRA_QVOLa = np.loadtxt("VOTGA_cycle_GTJRA_QVOLa.txt")

SSSGA_cycle_GTIAF_QVOLa = np.loadtxt("SSSGA_cycle_GTIAF_QVOLa.txt")
SSSGA_cycle_GTJRA_QVOLa = np.loadtxt("SSSGA_cycle_GTJRA_QVOLa.txt")
VOSGA_cycle_GTIAF_QVOLa = np.loadtxt("VOSGA_cycle_GTIAF_QVOLa.txt")
VOSGA_cycle_GTJRA_QVOLa = np.loadtxt("VOSGA_cycle_GTJRA_QVOLa.txt")

plt.tight_layout()
fig, ax = plt.subplots(4, 1, figsize=(20, 15), sharex="all")
fig.subplots_adjust(hspace=0.3)

ax[0].grid(linestyle='--')
ax[0].set_xlim([0, 371])
ax[0].set_ylim([17.8, 18.8])
ax[0].set_ylabel("Temperature [$\degree$C]")
ax[0].text(352, 18.7, "Unit: $\degree$C", fontsize=12)
ax[0].plot(SSTGA_cycle_GTIAF_QVOLa, lw=3, color='#0303FF')
ax[0].plot(SSTGA_cycle_GTJRA_QVOLa, lw=3, color='#FF0021')
ax[0].legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")

ax[0].axvline(61, linestyle='--', color='#0EA830')
ax[0].axvline(62, linestyle='--', color='#FF04FA')
ax[0].axvline(122, linestyle='--', color='#0EA830')
ax[0].axvline(124, linestyle='--', color='#FF04FA')
ax[0].axvline(183, linestyle='--', color='#0EA830')
ax[0].axvline(186, linestyle='--', color='#FF04FA')
ax[0].axvline(244, linestyle='--', color='#0EA830')
ax[0].axvline(248, linestyle='--', color='#FF04FA')
ax[0].axvline(305, linestyle='--', color='#0EA830')
ax[0].axvline(310, linestyle='--', color='#FF04FA')


ax[1].grid(linestyle='--')
ax[1].set_xlim([0, 371])
ax[1].set_ylim([3.5, 4.3])
ax[1].set_ylabel("Temperature [$\degree$C]")
ax[1].text(352, 4.235, "Unit: $\degree$C", fontsize=12)
ax[1].plot(VOTGA_cycle_GTIAF_QVOLa, lw=3, color='#0303FF')
ax[1].plot(VOTGA_cycle_GTJRA_QVOLa, lw=3, color='#FF0021')
ax[1].legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")

ax[1].axvline(61, linestyle='--', color='#0EA830')
ax[1].axvline(62, linestyle='--', color='#FF04FA')
ax[1].axvline(122, linestyle='--', color='#0EA830')
ax[1].axvline(124, linestyle='--', color='#FF04FA')
ax[1].axvline(183, linestyle='--', color='#0EA830')
ax[1].axvline(186, linestyle='--', color='#FF04FA')
ax[1].axvline(244, linestyle='--', color='#0EA830')
ax[1].axvline(248, linestyle='--', color='#FF04FA')
ax[1].axvline(305, linestyle='--', color='#0EA830')
ax[1].axvline(310, linestyle='--', color='#FF04FA')


ax[2].grid(linestyle='--')
ax[2].set_xlim([0, 371])
ax[2].set_ylim([33.96, 34.7])
ax[2].set_ylabel("Salinity [psu]")
ax[2].text(352, 34.64, "Unit: psu", fontsize=12)
ax[2].plot(SSSGA_cycle_GTIAF_QVOLa, lw=3, color='#0303FF')
ax[2].plot(SSSGA_cycle_GTJRA_QVOLa, lw=3, color='#FF0021')
ax[2].legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")

ax[2].axvline(61, linestyle='--', color='#0EA830')
ax[2].axvline(62, linestyle='--', color='#FF04FA')
ax[2].axvline(122, linestyle='--', color='#0EA830')
ax[2].axvline(124, linestyle='--', color='#FF04FA')
ax[2].axvline(183, linestyle='--', color='#0EA830')
ax[2].axvline(186, linestyle='--', color='#FF04FA')
ax[2].axvline(244, linestyle='--', color='#0EA830')
ax[2].axvline(248, linestyle='--', color='#FF04FA')
ax[2].axvline(305, linestyle='--', color='#0EA830')
ax[2].axvline(310, linestyle='--', color='#FF04FA')


ax[3].grid(linestyle='--')
ax[3].set_xlim([0, 372])
ax[3].set_ylim([34.7115, 34.715])
ax[3].set_ylabel("Salinity [psu]")
ax[3].text(352, 34.7147, "Unit: psu", fontsize=12)
ax[3].plot(VOSGA_cycle_GTIAF_QVOLa, lw=3, color='#0303FF')
ax[3].plot(VOSGA_cycle_GTJRA_QVOLa, lw=3, color='#FF0021')
ax[3].legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")
plt.yticks([34.7115, 34.7120, 34.7125, 34.7130, 34.7135, 34.7140, 34.7145, 34.7150],
           ["34.7115", "34.7120", "34.7125", "34.7130", "34.7135", "34.7140", "34.7145", "34.7150"])

ax[3].axvline(61, linestyle='--', color='#0EA830')
ax[3].axvline(62, linestyle='--', color='#FF04FA')
ax[3].axvline(122, linestyle='--', color='#0EA830')
ax[3].axvline(124, linestyle='--', color='#FF04FA')
ax[3].axvline(183, linestyle='--', color='#0EA830')
ax[3].axvline(186, linestyle='--', color='#FF04FA')
ax[3].axvline(244, linestyle='--', color='#0EA830')
ax[3].axvline(248, linestyle='--', color='#FF04FA')
ax[3].axvline(305, linestyle='--', color='#0EA830')
ax[3].axvline(310, linestyle='--', color='#FF04FA')

plt.savefig("six cycle (SST VOT SSS VOS).png")
plt.show()
