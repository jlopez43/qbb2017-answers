#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv( sys.argv[1], sep="\t" )
df2 = pd.read_csv( sys.argv[2], sep="\t" )



coi = "FPKM"
#np.log((df[coi]) + 1, (df2[coi] + 1))
x = np.log(df[coi] + 1)
y = np.log(df2[coi] + 1)



plt.figure()
plt.xlim((0, 10))
plt.ylim((0, 10))
plt.scatter( x, y, alpha=0.10, c = "red")
plt.suptitle( 'SRR072893 v SRR072915 FPKM values')
plt.xlabel( 'SRR072893')
plt.ylabel( 'SRR072915')

x2 = np.unique(x)
fit = np.polyfit(x,y,deg=1)
fit_func = np.poly1d(fit)
y2 = fit_func(x2)

plt.plot( x2, y2 )
plt.savefig( sys.argv[3] + ".png" )
plt.close()