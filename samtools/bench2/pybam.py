#!/usr/bin/env python 

import sys
import pysam

bamFileName = sys.argv[1]
bamfile = pysam.AlignmentFile(bamFileName)
#bamOutName = sys.argv[2]
#samout = pysam.AlignmentFile(bamOutName,"wb",header=bamfile.header)

count = 0
for align in bamfile:
    if align.mapping_quality > 20:
        #count+=1
        #print(align.query_name,"\t",align.query_alignment_length)
        #align.query_name = align.query_name.upper()
        #samout.write(align)
        count+=1

print("Count: ",count)

#time ./pybam.py testdata/smaller.bam output/py.bam
#real	0m45.674s

# Count only
# time pybam.py /Volumes/data/sim/jade/chr16only_jade.bam
# Count:  15548210
# real	0m27.665s
