#!/usr/bin/env python3 

import numpy as np
from numba import jit

# 9.13 seconds when vec is a native list
# 0.57 seconds when vec is a numpy array
def in_search(vec, x):
    return x in vec

# 0.57 seconds when vec is a numpy array
def vec_search(vec, x):
    return np.any(vec==x)

#  18.70 seconds when vec is a native list
# 121.48 seconds when vec is a numpy array
#   0.47 seconds when vec is a numpy array with numba @jit
def foreach_search(vec, x):
    for v in vec:
        if v == x:
            return True
    return False

#  40.75 seconds when vec is a native list
# 161.36 seconds when vec is a numpy array
#   0.55 seconds when vec is a numpy array with numba @jit
def for_search(vec, x):
    for i in range(len(vec)):
        if vec[i] == x:
            return True
    return False
    
