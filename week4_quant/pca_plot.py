#!/usr/bin/env python

import sys
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


pca = open(sys.argv[1])

x, y = [], []
for line in pca:
    scat = line.rstrip("\r\n").split(" ")
    x.append(float(scat[2]))
    y.append(float(scat[3]))
    
    #print scat



plt.figure()
plt.scatter(x, y)
plt.xlabel("pc1")
plt.ylabel("pc2")
plt.savefig("pca_plot.png")
plt.close()