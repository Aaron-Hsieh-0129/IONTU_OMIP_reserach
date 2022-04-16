import numpy as np
import h5py
import xarray as xr
import matplotlib.pyplot as plt

# IAF
data_IAF = h5py.File('/home/b08209006/IONTU/Zonal mean T_S/GTIAF_QVOLa.mat', 'r')


T0 = np.asarray(data_IAF['T0'])
T0_mean = np.nanmean(T0, axis=0)
T0_zonal_mean = np.nanmean(T0_mean, axis=2).swapaxes(0, 1)

zlev = np.asarray(data_IAF['zlev'][0])
lat = np.asarray(data_IAF['la0'][0])
xx, yy = np.meshgrid(lat, zlev)

plt.ylim(5304, 0)
plt.plot(xx, yy, T0_zonal_mean)
plt.show()