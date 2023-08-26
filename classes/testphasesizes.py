#!/usr/bin/env python

import hlapy.vcf as vcf
import sys
from collections import Counter

def getPS(fmt,sampleinfo):
    if "PS" in fmt:
        PSIdx = fmt.split(":").index("PS")
        ps = sampleinfo.split(":")[PSIdx]    

    return ps

def psSizes(vcfname):
    phasesetCounter = Counter()
    with open(vcfname) as vin:
        for line in vin:
            if line.startswith("#"): continue
            (chrom,loc,null1,ref,alt,qual,filt,info,fmt,sampleinfo) = line.strip().split("\t")
            # If there are no phase sets in the sample info just skip this variant
            ps = getPS(fmt,sampleinfo)
            if ps != ".":
                phasesetCounter.update([ps])
    
    return phasesetCounter
  
vcfname = sys.argv[1]
#phasesetCounter = psSizes(vcfname)
phasesetCounter = vcf.getPhaseSetSizes(vcfname)

print(phasesetCounter)

# chr6    1053851 .       T       C       10.2    PASS    .       GT:GQ:DP:AD:PQ:PD:PS    0|1:6:3:1,2:100:4:1053851
# chr6    1053852 .       A       G       14.5    PASS    .       GT:GQ:DP:AD:PQ:PD:PS    0|1:10:3:1,2:100:4:1053851
# chr6    1059114 .       C       G       14      PASS    .       GT:GQ:DP:AD:VAF:PL:PS   1/1:6:2:0,2:1:12,5,0:.
