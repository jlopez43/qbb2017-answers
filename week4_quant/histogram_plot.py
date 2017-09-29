#!/usr/bin/env python

import sys
import numpy as np
import math
import itertools
import matplotlib.pyplot as plt



ment = open(sys.argv[1])


freq = []

for i in ment:
    if i.startswith("#"):
        continue
    line = i.rstrip("\t\n").split()
    af = line[7]
    af1 = af[3:]
    if "," in af1:
        af2 = af1.split(",")
        for i in af2:
            freq.append(float(i))
    else:
        print af1
        freq.append(float(af1))


plt.figure()
plt.hist(freq, bins=80)
plt.savefig("Histogram_Plot.png")
plt.close()