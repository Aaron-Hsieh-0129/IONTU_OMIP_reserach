import numpy as np
import xarray as xr
import netCDF4 as nc

k = 0
TAUTOT8 = np.zeros([185, 420, 672])
QCLOUD = np.zeros([185, 40, 420, 672])
RAINNC = np.zeros([185, 420, 672])
for i in range(1, 4, 1):
    for j in range(1, 63, 1):
        if i != 3 and (j != 61 or j != 62):
            data = xr.open_dataset("/home/b08209006/IONTU/Dust/NASA_dust_wrf/postwrf_d01_2015%.6d"
                                   % int((10000 * (i + 6) + 100 * ((j + 1) // 2)) + 12 * ((j + 1) % 2)))
            TAUTOT8[k] = np.asarray(data['TAUTOT8'][0])
            QCLOUD[k] = np.asarray(data['QCLOUD'][0])
            RAINNC[k] = np.asarray(data['RAINNC'][0])
            k += 1
        else:
            data = xr.open_dataset("/home/b08209006/IONTU/Dust/NASA_dust_wrf/postwrf_d01_2015100100")
            TAUTOT8[k] = np.asarray(data['TAUTOT8'][0])
            QCLOUD[k] = np.asarray(data['QCLOUD'][0])
            RAINNC[k] = np.asarray(data['RAINNC'][0])
            break

data = xr.open_dataset("/home/b08209006/IONTU/Dust/NASA_dust_wrf/postwrf_d01_2015092900")
lon = np.asarray(data['XLONG'][0, :])
lat = np.asarray(data['XLAT'][:, 0])
PH = np.asarray(data['PH'][0, 1:, :, :])
PHB = np.asarray(data['PHB'][0, 0:40, :, :])

f_w = nc.Dataset('postwrf.nc', 'w', format='NETCDF4')
f_w.createDimension('time', 185)
f_w.createDimension('lev', 40)
f_w.createDimension('lat', 420)
f_w.createDimension('lon', 672)

f_w.createVariable('lat', np.float32, 'lat')
f_w.variables['lat'][:] = lat
f_w.createVariable('lon', np.float32, 'lon')
f_w.variables['lon'][:] = lon
f_w.createVariable('PH', np.float32, ('lev', 'lat', 'lon'))
f_w.variables['PH'][:] = PH
f_w.createVariable('PHB', np.float32, ('lev', 'lat', 'lon'))
f_w.variables['PHB'][:] = PHB
f_w.createVariable('TAUTOT8', np.float32, ('time', 'lat', 'lon'))
f_w.variables['TAUTOT8'][:] = TAUTOT8
f_w.createVariable('QCLOUD', np.float32, ('time', 'lev', 'lat', 'lon'))
f_w.variables['QCLOUD'][:] = QCLOUD
f_w.createVariable('RAINNC', np.float32, ('time', 'lat', 'lon'))
f_w.variables['RAINNC'][:] = RAINNC
f_w.close()
