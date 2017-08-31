#!/usr/bin/env python

"""
Usage: ./01-timecourse.py <samples.csv> <ctab_dir>

-Plot timecourse of FBtr0331261 for females
"""


import sys
import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

transcript = "FBtr0331261"


df_samples = pd.read_csv( sys.argv[1] )
soi = df_samples["sex"] == "female"

fpkms = []
for sample in df_samples["sample"][soi]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms.append( df[roi]["FPKM"].values )
    
soi2 = df_samples["sex"] == "male"
fpkms2 = []
for sample in df_samples["sample"][soi2]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms2.append( df[roi]["FPKM"].values )






df_replicates = pd.read_csv( sys.argv[3] )
soi3 = df_replicates["sex"] == "female"

fpkms3 = [None, None, None, None]
for sample in df_replicates["sample"][soi3]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms3.append( df[roi]["FPKM"].values )

soi4 = df_replicates["sex"] == "male"
fpkms4 = [None, None, None, None]
for sample in df_replicates["sample"][soi4]:
    fname = os.path.join(sys.argv[2], sample, "t_data.ctab" )
    df = pd.read_csv( fname, sep="\t")
    roi = df["t_name"] == transcript
    fpkms4.append( df[roi]["FPKM"].values )





plt.figure()
plt.plot( fpkms, c='red', lw=2 )
plt.plot( fpkms2, c='blue', lw=2 )
plt.plot( fpkms3, 'o', color='red', markersize=10 )
plt.plot( fpkms4, 'o', color='blue', markersize=10 )


#plt.scatter()
#plt.boxplot()
plt.suptitle( 'Sxl', fontsize=25 )
plt.xlabel( 'developmental stage', fontsize=15 )
plt.ylabel( 'Fragments Per Kilobase of transcript per Million (FPKM)', fontsize=15 )
art=[]
plt.gca().tick_params(direction='out', top='off', right='off' )
plt.xticks( range(8), ('10', '11', '12', '13', '14A', '14B', '14C', '14D'), rotation=90 )
plt.legend(['female', 'male', 'female replicates', 'male replicates'], loc='center right', bbox_to_anchor=(1.5,0.5), frameon = False, numpoints=1)
plt.savefig( "day4-homework.png", additional_artists=art, bbox_inches="tight" ) 
plt.close()












