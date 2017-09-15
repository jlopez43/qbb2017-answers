#!/usr/bin/env python2.7

import sys
import fasta
import itertools
import numpy as np
import pandas as pd


nuc = open(sys.argv[1])
amino = open(sys.argv[2])
align = open("alignment_nucleotide.fa", "w")


for (nt_i, nt_s), (prot_i, prot_s) in itertools.izip(fasta.FASTAReader(nuc), fast.FASTAReader(amino)):
    realign.write(nt_i + "\n")
    for aa in prot_s:
        if aa == "-":
            realign.write("---")
        else:
            realign.write(nt_s[:3])
            nt_s = nt_s[3:]