#!/usr/bin/env julia

using Statistics

fname = ARGS[1]


function readvec(filename)
    open(filename, "r") do f
        map(line -> parse(Int, line), eachline(f))
    end
end

a = readvec(fname)

println("Average value is: ",mean(a))

# time ./meanvec2.jl bigvec.txt
# Average value is: 1.000092714825e6
# ./meanvec2.jl bigvec.txt  8.15s user 0.74s system 101% cpu 8.794 total

# So, not really better than the much less obscure version.