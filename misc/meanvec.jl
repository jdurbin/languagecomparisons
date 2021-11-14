#!/usr/bin/env julia

using Statistics

filename = ARGS[1]

a = Int[]
open(filename,"r") do f
	for line in eachline(f)
		push!(a,parse(Int,line))
	end
end

println("Mean value is: ",mean(a))


# time ./meanvec.jl vec.txt
# Average value is: 1.000092714825e6
# ./meanvec.jl vec.txt  0.81s user 0.25s system 111% cpu 0.950 total

# bigvec.txt: 40,000,000
# time ./meanvec.jl bigvec.txt
# Average value is: 1.000092714825e6
# ./meanvec.jl bigvec.txt  8.61s user 1.11s system 99% cpu 9.742 total

