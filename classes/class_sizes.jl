#!/user/bin/env julia 

struct GeneCounts
    gene::String
    count1::Int
    count2::Int
end

l = [GeneCounts("HLA-A", rand(0:9), rand(0:9)) for i in 1:50000000]

println("Record the RAM and hit any key.")
readline()


# This code is virtually identical to the Python code, down to the list comprehension. 
# Pretty low cost for 80X speedup and 6X space reduction. 

# Macbook Pro M1
# 1,000,000		131MB	131 bytes/ea   CPU 2.43s  
# 10,000,000	336MB	34 bytes/ea    CPU 2.52s
# 50,000,000	1.22GB	24 bytes/ea    CPU 2.91s  2.42 JIT + 0.0098us/ea
# Line: 2.42s + .0098us/each