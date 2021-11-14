#!/usr/bin/env python3

import numpy as np
import sys

def readvec(filename):
    a=[]
    with open(filename) as fin:
        for line in fin:
                a.append(float(line))

    return a

def distances_among_pairs_loop(v):
    nin = len(v)
    nout = (nin*nin) // 2
    dists = np.zeros(nout)
    k=0
    for i in range(0,nin-1):
        a = v[i]
        for j in range(i+1,nin):
            b=v[j]
            dists[k]=abs(a-b)
            k+=1
    
    return dists


vin = readvec(sys.argv[1])
distances = distances_among_pairs_loop(vin)


# time ./pairdist.py vec1.txt
# ./pairdist.py vec1.txt  8.97s user 0.24s system 97% cpu 9.413 total