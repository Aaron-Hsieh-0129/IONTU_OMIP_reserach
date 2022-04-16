import numpy as np

SST_bias_IAF = np.loadtxt("SST_bias_IAF.txt")

for i in range(288 - 1):
    for j in range(320 - 1):
        if np.isnan(SST_bias_IAF[i + 1, j]) and (~np.isnan(SST_bias_IAF[i, j])) and \
                np.isnan(SST_bias_IAF[i - 1, j]) and np.isnan(SST_bias_IAF[i, j + 1]) and \
                np.isnan(SST_bias_IAF[i, j - 1]):
            print("i=%d, j=%d" % (j, i))
