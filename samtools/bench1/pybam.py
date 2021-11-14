#!/usr/bin/env python 

import sys
import pysam

bamFileName = sys.argv[1]
samfile = pysam.AlignmentFile(bamFileName)

count = 0
for align in samfile:
    if align.mapping_quality > 20:
        count+=1
        #print(align.query_name,"\t",align.query_alignment_length)

print("Count: ",count)

# Test for quality > 50 and write out name/quality
# real	0m5.649s


# Larger file: testdata/wtdbg2_ont40x_vs_haplotigs_map-ont.bam
# real	0m14.219s
# Results: 1,192,853