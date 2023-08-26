#!/usr/bin/env python3

from dataclasses import dataclass
from random import randrange

# Are the class definitions in phasedtypes.py overkill? 
# 
# I get mixed messages about how much people use objects in Python.   In C++ or Java it's natural 
# that bits of data that travel around as a unit should be an object.  In Python people more often 
# seem to just use tuples, dictionaries, lists and compositions of these.  It feels like most Python 
# programmers avoid objects.  To me the Python syntax for classes also feels like an after-thought which 
# reinforces the feeling that it's 2nd class. I have also had the impression that Python classes were 
# inefficient, which could be another factor if true.  To see if it's true I did a simple test creating 
# list of 50 million objects with a string and two ints as fields, a list of 50 million similar tuples, 
# and finally a list of 50 million objects in groovy for baseline:  
# 
#                 bytes/ea    microseconds/ea  totaltime(incl warmup)  groovyrelative
# Python object   150         0.8               41.0s                   4.8X slower than Groovy 
# Python tuple    62          0.5               25.0s                   3X   slower than Groovy 
# Groovy object   62          0.17               8.5s                   1X   Groovy 
# Julia struct    24          0.0098             2.4s                   3.5X faster than Groovy wall clock
#                                                                       17X  faster than Groovy per record.
#                                                                       51X  faster than Python tuple. 
#                                                                       81X  faster than Python object 
#
# So it's a bit inefficient but not prohibitively so compared to something like Groovy.  Of course, 
# efficiency doesn't matter for this application, but if it were grossly inefficient it could be a 
# reason to avoid classes as a routine. 


@dataclass 
class GeneCounts:
    gene: str
    count1: int
    count2: int
    
l = [GeneCounts("HLA-A",randrange(10),randrange(10)) for i in range(50000000)]

input("Record the RAM and hit any key.")

# Macbook Pro M1
#  1,000,000 168MB  168 bytes/ea   CPU: 0.85s  0.85us/ea
# 10,000,000 1.5GB  150 bytes/ea   CPU: 8.3s   0.83us/ea
# 50,000,000 7.53GB 151 bytes/ea   CPU: 41s    0.82us/ea
# Line: .82 us/ea