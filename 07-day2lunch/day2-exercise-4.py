#!/usr/bin/env python

import sys

align = open(sys.argv[1])

time = align.readlines()

result = []

for line in time:
    if "AS:" not in line:
        continue
    else:
        result.append(line.split("\t")[2])
        
align.close()
print result[0:10]
    
