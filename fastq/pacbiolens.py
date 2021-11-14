#!/usr/bin/env python3
import sys, numpy as np

# Read name format is:
# @m64044_200216_052200/10/0_7188

fastqfile = sys.argv[1]
readlengths = []
with open(fastqfile) as fqin:
    for line in fqin:
        if line.startswith("@"):
            runtime_barcode,ZMW_hole,subread_region = line.split("/")
            sstart,send = subread_region.split("_") # in polymerase read coordinates
            readlength = int(send)-int(sstart)
            readlengths.append(readlength)

print(f"Total bases: {np.sum(readlengths)}")  
    
# time ./pacbiolens.py vespula_germanica_first1Mlines_subreads.fastq
# Total bases: 5972061831
# ./pacbiolens.py vespula_germanica_first1Mlines_subreads.fastq  6.50s user 3.90s system 93% cpu 11.133 total