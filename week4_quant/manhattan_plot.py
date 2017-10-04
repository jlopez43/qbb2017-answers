#!/usr/bin/env python

import sys
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt



manp = open(sys.argv[1])


sig = []
notsig = []

lines = 5
for i in manp:
    fields = i.split()
    if "CHR" in i:
        continue
    elif "NA" in i:
        continue
    lines += 1
for i in range(lines):
    sig.append(None)
    notsig.append(None)
    

count = 0
manp.seek(0)

for i in manp:
    fields = i.split()
    if "CHR" in i:
            continue
    elif "NA" in i:
        continue
    elif "ADD" not in i:
        continue
    elif float(fields[8]) <= 10e-5:
        sig[count] = -np.log10(float(fields[8]))
        count += 1
    elif float(fields[8]) > 10e-5:
        notsig[count] = -np.log10(float(fields[8]))
        count += 1





plt.figure()
plt.scatter(range(len(sig)),sig,s=5,alpha=.6,c= "green")
plt.scatter(range(len(sig)),notsig,s=5, alpha=.6,c = "orange")
plt.savefig(str(sys.argv[2]) + "Manhattan_Plot.png")
plt.close()





