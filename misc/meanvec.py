#!/usr/bin/env python3

import sys
from statistics import mean

filename = sys.argv[1]
a=[]
with open(filename) as fin:
    for line in fin:
            a.append(int(line))
    
print("Mean value is: ",mean(a))


# time ./meanvec.py vec.txt
# Mean value is:  1000092.714825
# ./meanvec.py vec.txt  0.70s user 0.05s system 75% cpu 0.986 total


# bigvec.txt: 40,000,000
# time ./meanvec.py bigvec.txt
# Mean value is:  1000092.714825
# ./meanvec.py bigvec.txt  26.05s user 0.91s system 98% cpu 27.301 total