#!/usr/bin/env python3 

import seaborn as sns
import pysam,sys

bamName = sys.argv[1]
plotName = sys.argv[2]

def histQuals(bamInName):
    allquals=[]
    bamIn = pysam.AlignmentFile(bamInName)
    print("Reading BAM")
    for a in bamIn:
        allquals.append(a.mapping_quality)

    print("Plotting")
    return sns.histplot(allquals)
    
hist = histQuals(bamName)
hist.figure.savefig(plotName)

# time ./qualhist.py data/PC-HLA-EG4.bam histpy.png
# Reading BAM
# Plotting
# 1.22s user 0.42s system 66% cpu 2.446 total


# time qualhist.py /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam histpy.png
# Reading BAM
# Plotting
# qualhist.py /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam histpy.png  
# 18.19s user 0.93s system 98% cpu 19.359 total


# This implies:
# Warmup time 0.95 sec .
# Time to complete after warmup: 17.06 sec

