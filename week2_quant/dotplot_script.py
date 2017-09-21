#!/usr/bin/env python

import sys
import fasta
import itertools
import numpy as np
import pandas as pd
import operator
import matplotlib.pyplot as plt


ref = open(sys.argv[1])
#contig = open(sys.argv[2])


lencount = 0

for line in ref:
    lencount += 1
    if lencount == 1:
        pass
    else:
        fields = line.rstrip("\r\n").split("\t")
        plt.plot([lencount,lencount+(float(fields[1])-float(fields[0]))],[float(fields[0]),float(fields[1])])
        lencount += float(fields[1])-float(fields[0])
    
    
plt.xlim(0,100000)
plt.ylim(0,100000)
plt.xlabel("contigs")
plt.ylabel("position")
#plt.savefig("lastz spades dotplot")
#plt.savefig("lastz velvet dotplot")
#plt.savefig("lastz nanopore dotplot")
#plt.savefig("better coverage dotplot")
#plt.savefig("better coverage dotplot velvet")