import numpy as np
import xarray as xr
import netCDF4 as nc

k = 0
aice = np.zeros([4464, 288, 320])
for i in range(1, 373, 1):
    for j in range(1, 13, 1):
        data = xr.open_dataset("/home/b08209006/IONTU/SIC/yht_GTIAF_QVOLa/GTIAF_QVOLa.cice.h.0%.3d-%.2d.nc" % (i, j))
        aice[k, :, :] = np.asarray(data['aice'][0])
        k += 1

lon = np.asarray(data['TLON'][0, :])
lat = np.asarray(data['TLAT'][:, 0])

f_w = nc.Dataset('aice_omip2_yht_GTIAF_QVOLa.nc', 'w', format='NETCDF4')
f_w.createDimension('time', 4464)
f_w.createDimension('lat', 288)
f_w.createDimension('lon', 320)

f_w.createVariable('lat', np.float32, 'lat')
f_w.variables['lat'][:] = lat
f_w.createVariable('lon', np.float32, 'lon')
f_w.variables['lon'][:] = lon
f_w.createVariable('aice', np.float32, ('time', 'lat', 'lon'))
f_w.variables['aice'][:] = aice
f_w.close()
