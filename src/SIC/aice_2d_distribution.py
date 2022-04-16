import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio
import matplotlib.cm as cm


def Annual_mean(aice, years):
    aice_annual_mean = np.zeros([years, 288, 320])
    for i in range(years):
        aice_annual_mean[i] = sum(aice[i * 12:(i + 1) * 12]) / 12
    return aice_annual_mean


data_area = sio.loadmat("areaGd.mat")
areaGd = np.asarray(data_area['areaGd']).swapaxes(0, 1)

data_IAF = xr.open_dataset("aice_omip2_yht_GTIAF_QVOLa.nc")
aice_IAF = np.asarray(data_IAF['aice'])

data_JRA = xr.open_dataset("aice_omip2_yht_GTJRA_QVOLa.nc")
aice_JRA = np.asarray(data_JRA['aice'])

year_IAF = 372
aice_IAF = Annual_mean(aice_IAF, year_IAF)
aice_IAF /= 100
aice_IAF_area_array = aice_IAF * areaGd

for i in range(62):
    a = plt.contourf(aice_IAF_area_array[310+i], cmap=cm.Blues, levels=np.arange(0, 4.8*10**9+5*10**8, 5*10**8))
    plt.title("IAF_%d" % (i+1948))
    plt.colorbar(a)
    plt.savefig("IAF_%d.png" % (i+1948))
    plt.show()
    plt.close()

year_JRA = 366
aice_JRA = Annual_mean(aice_JRA, year_JRA)
aice_JRA /= 100
aice_JRA_area_array = aice_JRA * areaGd

for i in range(61):
    a = plt.contourf(aice_JRA_area_array[305+i], cmap=cm.Blues, levels=np.arange(0, 4.8*10**9+5*10**8, 5*10**8))
    plt.title("JRA_%d" % (i+1958))
    plt.colorbar(a)
    plt.savefig("JRA_%d.png" % (i+1958))
    plt.show()
    plt.close()