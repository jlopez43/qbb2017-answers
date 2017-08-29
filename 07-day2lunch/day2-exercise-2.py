#!/usr/bin/env python

import sys

##fh = open( "/Users/cmdb/data/genomes/893_alignment.sam")
fh = sys.stdin
# fh = open(sys.argv[1])

string = "NM:i:0"
count = 0


for line in fh:
    if string in line:
        count = count + 1

print count