import numpy as np

fo = open('file.txt', 'w+')

for j in range(1, 166):
    for i in range(1, 13):
        fo.write("https://www1.ncdc.noaa.gov/pub/data/cmb/ersst/v5/netcdf/ersst.v5.%.4d%.2d.nc " % (1853 + j, i))
