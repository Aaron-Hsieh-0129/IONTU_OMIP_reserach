import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

# IAF
data_IAF = h5py.File('/home/b08209006/IONTU/Drift/GTIAF_QVOLa.mat', 'r')
T = np.asarray(data_IAF['thetao'])
T_1 = T[0]
T_drift = np.asarray([T[i] - T_1 for i in range(372)]).swapaxes(0, 1)
zlev = np.asarray(data_IAF['zlev'][0])
x = np.arange(0, 372, 1)
xx, yy = np.meshgrid(x, zlev)

plt.tight_layout()
plt.figure(figsize=(12, 8), dpi=300)
plt.ylim(1200, 0)
ax = plt.contourf(xx, yy, T_drift, cmap=cm.RdYlBu_r, levels=np.arange(-0.5, 3 + 0.1, 0.1))
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdYlBu_r), orientation="horizontal", extend='both',
             spacing='uniform', pad=0.1, aspect=27, boundaries=np.arange(-0.5, 3 + 0.1, 0.1))
plt.yticks([0, 200, 400, 600, 800, 1000, 1200], ["0", "0.2", "0.4", "0.6", "0.8", "1", "1.2"])
cn1 = plt.contour(xx, yy, T_drift, colors='k', levels=np.arange(-0.5, 3 + 0.2, 0.2))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.show()


# JRA
data_JRA = h5py.File('/home/b08209006/IONTU/Drift/GTJRA_QVOLa.mat', 'r')
T = np.asarray(data_JRA['thetao'])
T_1 = T[0]
T_drift = np.asarray([T[i] - T_1 for i in range(366)]).swapaxes(0, 1)
zlev = np.asarray(data_JRA['zlev'][0])
x = np.arange(0, 366, 1)
xx, yy = np.meshgrid(x, zlev)

plt.tight_layout()
plt.figure(figsize=(12, 8), dpi=300)
plt.ylim(1200, 0)
ax = plt.contourf(xx, yy, T_drift, cmap=cm.RdYlBu_r, levels=np.arange(-0.8, 2 + 0.1, 0.1))
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdYlBu_r), orientation="horizontal", extend='both',
             spacing='uniform', pad=0.1, aspect=27, boundaries=np.arange(-0.8, 2 + 0.1, 0.1))
plt.yticks([0, 200, 400, 600, 800, 1000, 1200], ["0", "0.2", "0.4", "0.6", "0.8", "1", "1.2"])
cn1 = plt.contour(xx, yy, T_drift, colors='k', levels=np.arange(-0.8, 2 + 0.2, 0.2))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.1f")
plt.show()
