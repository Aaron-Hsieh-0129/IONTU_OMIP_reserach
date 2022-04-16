import h5py
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib as mpl

# IAF
data_IAF = h5py.File('/home/b08209006/IONTU/Drift/GTIAF_QVOLa.mat', 'r')
S = np.asarray(data_IAF['so'])
S_1 = S[0]
S_drift = np.asarray([S[i] - S_1 for i in range(372)]).swapaxes(0, 1)
S_drift = np.where(S_drift <= -0.25, -0.25, S_drift)
zlev = np.asarray(data_IAF['zlev'][0])
x = np.arange(0, 372, 1)
xx, yy = np.meshgrid(x, zlev)

plt.tight_layout()
plt.figure(figsize=(12, 8), dpi=300)
plt.ylim(1200, 0)
ax = plt.contourf(xx, yy, S_drift, cmap=cm.RdYlBu_r, levels=np.arange(-0.25, 0.25 + 0.02, 0.02))
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdYlBu_r), orientation="horizontal", extend='both',
             spacing='uniform', pad=0.1, aspect=27, boundaries=np.arange(-0.25, 0.25 + 0.02, 0.02))
plt.yticks([0, 200, 400, 600, 800, 1000, 1200], ["0", "0.2", "0.4", "0.6", "0.8", "1", "1.2"])
cn1 = plt.contour(xx, yy, S_drift, colors='k', levels=np.arange(-0.25, 0.25 + 0.02, 0.02))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.2f")
plt.show()

# JRA
data_JRA = h5py.File('/home/b08209006/IONTU/Drift/GTJRA_QVOLa.mat', 'r')
S = np.asarray(data_JRA['so'])
S_1 = S[0]
S_drift = np.asarray([S[i] - S_1 for i in range(366)]).swapaxes(0, 1)
zlev = np.asarray(data_JRA['zlev'][0])
x = np.arange(0, 366, 1)
xx, yy = np.meshgrid(x, zlev)

plt.tight_layout()
plt.figure(figsize=(12, 8), dpi=300)
plt.ylim(1200, 0)
ax = plt.contourf(xx, yy, S_drift, cmap=cm.RdYlBu_r, levels=np.arange(-0.5, 0.2 + 0.02, 0.02))
plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdYlBu_r), orientation="horizontal", extend='both',
             spacing='uniform', pad=0.1, aspect=27, boundaries=np.arange(-0.5, 0.2 + 0.02, 0.02))
plt.yticks([0, 200, 400, 600, 800, 1000, 1200], ["0", "0.2", "0.4", "0.6", "0.8", "1", "1.2"])
cn1 = plt.contour(xx, yy, S_drift, colors='k', levels=np.arange(-0.5, 0.2 + 0.02, 0.02))
plt.clabel(cn1, inline=1, fontsize=10, fmt="%1.2f")
plt.show()
