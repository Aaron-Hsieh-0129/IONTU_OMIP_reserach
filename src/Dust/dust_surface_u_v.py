import numpy as np
import xarray as xr
import matplotlib.pyplot as plt

import cartopy.crs as ccrs
import matplotlib.cm as cm
import cartopy.feature as cfeature
import matplotlib as mpl

data_YRYM = xr.open_dataset("YRYM_Ernesto_ocean_his_d01.nc")
data_NRNM = xr.open_dataset("NRNM_Ernesto_ocean_his_d01.nc")
# data_wolf = xr.open_dataset("Wolf_YRYM_dust.nc")
# dust = np.asarray(data_wolf['DUST_1'][0])

lon = np.asarray(data_YRYM['lon_psi'][:, :])
lat = np.asarray(data_YRYM['lat_psi'][:, :])

u_YRYM = np.asarray(data_YRYM['u'][60:, 24, 1:, :])  # from 2015070100~2015100100
v_YRYM = np.asarray(data_YRYM['v'][60:, 24, :, 1:])

u_NRNM = np.asarray(data_NRNM['u'][60:, 24, 1:, :])
v_NRNM = np.asarray(data_NRNM['v'][60:, 24, :, 1:])

plt.tight_layout()
plt.figure(dpi=500, figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree(central_longitude=lon[0, 435]))
ax.coastlines(resolution='110m')
ax.gridlines()
ax.add_feature(cfeature.LAND)
ax.quiver(lon[::10, ::10], lat[::10, ::10], u_YRYM[0, ::10, ::10], v_YRYM[0, ::10, ::10],
          pivot='mid', width=0.001, scale=30, headwidth=5)
plt.show()
