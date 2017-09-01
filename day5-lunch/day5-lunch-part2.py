#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm


df = pd.read_csv( sys.argv[1], sep="\t" )
df27 = pd.read_csv( sys.argv[2], sep="\t", header=None)
df36 = pd.read_csv( sys.argv[3], sep="\t", header=None )
df4 = pd.read_csv( sys.argv[4], sep="\t", header=None )
df9 = pd.read_csv( sys.argv[5], sep="\t", header=None )


fpkm = df["FPKM"]
h3k27 = df27[5]
h3k36 = df36[5]
h3k4 = df4[5]
h3k9 = df9[5]


combine = pd.concat([h3k27, h3k36, h3k4, h3k9], axis = 1)

model = sm.OLS(fpkm, combine)
results = model.fit()



print (results.summary())


#pt = pd.concat([fpkm, h3k27, h3k36, h3k4, h3k9])
#print pt

#ts = df["0.3"]
#print fpkm
#
# plt.figure()
# plt.scatter()
# plt.savefig()
# plt.close()