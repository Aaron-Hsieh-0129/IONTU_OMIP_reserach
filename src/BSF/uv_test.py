import numpy as np
import xarray as xr
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib.cm as cm
import cartopy.feature as cfeature
import matplotlib as mpl

IAF_u = xr.open_dataset("/home/b08209006/IONTU/BSF/IAF_uo/uo_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
IAF_v = xr.open_dataset("/home/b08209006/IONTU/BSF/IAF_vo/vo_Omon_TaiESM1-TIMCOM_omip1_r1i1p1f1_gn_031101-037212.nc")
JRA_u = xr.open_dataset("/home/b08209006/IONTU/BSF/JRA_uo/uo_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")
JRA_v = xr.open_dataset("/home/b08209006/IONTU/BSF/JRA_vo/vo_Omon_TaiESM1-TIMCOM_omip2_r1i1p1f1_gn_030601-036612.nc")
data_depth = xr.open_dataset("/home/b08209006/IONTU/BSF/deptho.nc")

lev = np.asarray(IAF_u['lev_bnds'])
dz = lev[:, 1] - lev[:, 0]
lon = np.asarray(IAF_u['nlon'])
lat = np.asarray(IAF_u['nlat'])
lon, lat = np.meshgrid(lon, lat)
depth = np.asarray(data_depth['deptho'])

u_IAF_weighted_annual_mean = np.zeros([52, 288, 320])
v_IAF_weighted_annual_mean = np.zeros([52, 288, 320])
u_JRA_weighted_annual_mean = np.zeros([52, 288, 320])
for i in range(52):
    u_IAF = np.asarray(IAF_u['uo'][120 + 12 * i:132 + 12 * i, :, :, :])
    u_annual_mean = np.nanmean(u_IAF, axis=0)
    # masked_data = np.ma.masked_array(u_annual_mean, np.isnan(u_annual_mean))
    u_IAF_weighted_annual_mean[i] = np.nansum(np.asarray([dz[j]*u_annual_mean[j] for j in range(45)]), axis=0) / depth

    # v_IAF = np.asarray(IAF_v['vo'][120 + 12 * i:132 + 12 * i, :, :, :])
    # v_annual_mean = np.nanmean(v_IAF, axis=0)
    # masked_data = np.ma.masked_array(v_annual_mean, np.isnan(v_annual_mean))
    # v_weighted_annual_mean[i] = np.ma.average(masked_data, axis=0, weights=dz)

    u_JRA = np.asarray(JRA_u['uo'][120 + 12 * i:132 + 12 * i, :, :, :])
    u_annual_mean = np.nanmean(u_JRA, axis=0)
    # masked_data = np.ma.masked_array(u_annual_mean, np.isnan(u_annual_mean))
    u_JRA_weighted_annual_mean[i] = np.nansum(np.asarray([dz[j]*u_annual_mean[j] for j in range(45)]), axis=0) / depth


u_IAF_ave = np.average(u_IAF_weighted_annual_mean, axis=0)
u_JRA_ave = np.average(u_JRA_weighted_annual_mean, axis=0)

plt.tight_layout()
plt.figure(dpi=500, figsize=(10, 6))
ax1 = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax1.coastlines(resolution='110m')
ax1.gridlines()
ax1.add_feature(cfeature.LAND)
ax1.contourf(lon, lat, u_IAF_ave, cmap=cm.RdBu_r, transform=ccrs.PlateCarree(), levels=np.arange(-30, 30 + 1, 1))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-30, 30 + 1, 1))
plt.show()


plt.tight_layout()
plt.figure(dpi=500, figsize=(10, 6))
ax2 = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax2.coastlines(resolution='110m')
ax2.gridlines()
ax2.add_feature(cfeature.LAND)
ax2.contourf(lon, lat, u_JRA_ave, cmap=cm.RdBu_r, transform=ccrs.PlateCarree(), levels=np.arange(-30, 30 + 1, 1))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-30, 30 + 1, 1))
plt.show()


plt.tight_layout()
plt.figure(dpi=500, figsize=(10, 6))
bias = u_JRA_ave - u_IAF_ave
ax3 = plt.axes(projection=ccrs.Robinson(central_longitude=180))
ax3.coastlines(resolution='110m')
ax3.gridlines()
ax3.add_feature(cfeature.LAND)
ax3.contourf(lon, lat, bias, cmap=cm.RdBu_r, transform=ccrs.PlateCarree(), levels=np.arange(-5, 5 + 0.2, 0.2))
cbar = plt.colorbar(mpl.cm.ScalarMappable(cmap=cm.RdBu_r), orientation="horizontal", extend='both',
                    spacing='uniform', pad=0.1, shrink=0.75, aspect=27, boundaries=np.arange(-5, 5 + 0.2, 0.2))

plt.show()
