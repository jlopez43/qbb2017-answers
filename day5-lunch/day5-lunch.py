#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv( sys.argv[1], sep="\t" )
df["up"] = df["end"] + 500
df["down"] = df["end"] - 500
coi = df[ [ "chr", "strand", "start", "end", "t_name", "up", "down"] ]

#print coi

plus = coi[ "strand" ] == "+"
df_plus = df[plus]


minus = coi[ "strand" ] == "-"
df_minus = df[minus]

# df_plus["up"] = [coi["end"] + 500]

# print df_plus["up"]

df_plus["up"] = df_plus["start"] - 500
df_plus["down"] = df_plus["start"] + 500

df_minus["up"] = df_minus["end"] - 500
df_minus["down"] = df_minus["end"] + 500

df = pd.concat([df_plus, df_minus])

toi = ["chr", "up", "down", "t_name"]

df[toi].to_csv(sys.argv[2], sep="\t", header=False, index=False)



# plt.figure()
# plt.scatter( x[:,0], x[:,1], alpha=0.8, c=sexes )
# plt.savefig( sys.argv[2] )
# plt.close()