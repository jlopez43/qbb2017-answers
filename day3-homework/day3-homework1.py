#!/usr/bin/env python

import sys
import fasta

fh1 = open(sys.argv[1]) #subset.fa.  target
fh2 = open(sys.argv[2]) #droyak       query
#fh3 = open(sys.argv[3]) #k which is the k-mer size.     k

count = 0

k = 11
kmer_counts = {}
ident, sequence = fasta.FASTAReader( fh2 ).next()

for ident, sequence in fasta.FASTAReader( fh1 ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer1 = sequence[i:i+k]
        if kmer1 not in kmer_counts:
            kmer_counts[kmer1] = [(ident, i)]
        else:
            kmer_counts[kmer1].append( (ident, i) )
            
for ident, sequence in fasta.FASTAReader( fh2 ):
    sequence = sequence.upper()
    for i in range( 0, len(sequence) - k ):
        kmer2 = sequence[i:i+k]
        if kmer2 in kmer_counts:
            for value in kmer_counts[kmer2]:
                count += 1
                if count > 1000:
                    break
                
                print('\t'.join((str(value[0]), str(value[1]), str(i), str(kmer2))))
            
            #print kmer_counts[kmer2], i, kmer2
        
        
        #
        # if kmer2 not in kmer_counts:
        #     kmer_counts[kmer2] = [(ident, i)]
        # else:
        #     kmer_counts[kmer2].append( (ident, i) )
        #
            
# for kmer, count in kmer_counts.iteritems():
#     if kmer1 in kmer2:
#         print kmer, count
#
#