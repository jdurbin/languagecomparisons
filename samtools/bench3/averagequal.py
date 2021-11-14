#!/usr/bin/env python3 
import pysam,sys
from statistics import mean
bamName = sys.argv[1]

def histQuals(bamInName):
    allquals=[]
    bamIn = pysam.AlignmentFile(bamInName)
    for a in bamIn:
        allquals.append(a.mapping_quality)

    print("Mean quality: ",mean(allquals))
    
histQuals(bamName)





# time averagequal.py /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam
# Reading BAM
# Average quality:  43.76016208794757
# averagequal.py /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam 
# 16.36s user 0.31s system 99% cpu 16.803 total


# time averagequal.py data/PC-HLA-EG4.bam
# Reading BAM
# Average quality:  56.078356406954285
# averagequal.py data/PC-HLA-EG4.bam  0.10s user 0.03s system 45% cpu 0.297 total

