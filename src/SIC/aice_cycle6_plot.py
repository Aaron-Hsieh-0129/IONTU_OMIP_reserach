import numpy as np
import matplotlib.pyplot as plt

aice_cycle_GTIAF_QVOLa_n = np.loadtxt("aice_cycle_GTIAF_QVOLa_n.txt")
aice_cycle_GTIAF_QVOLa_s = np.loadtxt("aice_cycle_GTIAF_QVOLa_s.txt")
aice_cycle_GTJRA_QVOLa_n = np.loadtxt("aice_cycle_GTJRA_QVOLa_n.txt")
aice_cycle_GTJRA_QVOLa_s = np.loadtxt("aice_cycle_GTJRA_QVOLa_s.txt")

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
# plt.ylim([17.8, 18.8])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [km$^2$]")
# plt.text(67, 18.725, "Unit: $\degree$C", fontsize=12)
plt.plot(np.arange(0, 62, 1), aice_cycle_GTIAF_QVOLa_n[310:] / 10**12, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), aice_cycle_GTJRA_QVOLa_n[305:] / 10**12, lw=3, color='#FF0021')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")
plt.title("North")
plt.show()

plt.tight_layout()
plt.figure(figsize=(15, 4))
plt.grid(linestyle='--')
plt.xlim([0, 71])
# plt.ylim([17.8, 18.8])
plt.xticks([2, 12, 22, 32, 42, 52, 62], ['1950', '1960', '1970', '1980', '1990', '2000', '2010'])
plt.ylabel("Volume [km$^2$]")
# plt.text(67, 18.725, "Unit: $\degree$C", fontsize=12)
plt.plot(np.arange(0, 62, 1), aice_cycle_GTIAF_QVOLa_s[310:] / 10**12, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), aice_cycle_GTJRA_QVOLa_s[305:] / 10**12, lw=3, color='#FF0021')
plt.legend(['IAF (1948~2009)', 'JRA (1958~2018)'], loc="upper left")
plt.title("South")
plt.show()