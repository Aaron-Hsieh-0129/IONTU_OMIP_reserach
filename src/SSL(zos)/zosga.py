import h5py
import matplotlib.pyplot as plt
import numpy as np

data_IAF = h5py.File("/home/b08209006/IONTU/SSL(zos)/GTIAF_QVOLa_zossga.mat", 'r')
data_JRA = h5py.File("/home/b08209006/IONTU/SSL(zos)/GTJRA_QVOLa_zossga.mat", 'r')
zosga_IAF = np.asarray(data_IAF['zossga'])
zosga_JRA = np.asarray(data_JRA['zossga'])

plt.plot(np.arange(0, 62, 1), zosga_IAF, lw=3, color='#0303FF')
plt.plot(np.arange(10, 71, 1), zosga_JRA, lw=3, color='#FF0021')

plt.show()