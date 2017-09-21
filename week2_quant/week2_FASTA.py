#!/usr/bin/env python

import sys
import fasta
import itertools
import numpy as np
import pandas as pd
import operator

#fox = open(sys.argv[1])
#hound = open(sys.argv[2])



total_l = 0
contigs = []


for name, seq in fasta.FASTAReader( open( sys.argv[1] )):
    if len(seq) == 0:
        pass
    else:
        sub = [name, seq, len(seq)]
        total_l += len(seq)
        contigs.append(sub)





#print contigs
contigs = sorted(contigs, key=operator.itemgetter(2), reverse=True)
#print contigs
print 'num contigs = %d' % ( len(contigs) )
print 'max contig = %d' % ( contigs [0][2] )
print 'min contig = %d' % ( contigs [-1][2])
print 'avg contig = %f' % ( float(total_l) / float(len(contigs)))



ldiv = float(total_l) / 2.0

tot = 0
for each in contigs:
    tot += each[2]
    if tot >= ldiv:
        n50 = each
        break






print 'N50 = %d' % ( n50[2] ) 







