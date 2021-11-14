#!/usr/bin/env julia


function readvec(filename)
	a = Float64[]
	open(filename,"r") do f
		for line in eachline(f)
			push!(a,parse(Float64,line))
		end
	end
	return a
end


function distances_among_pairs_loop(v)
    nin = length(v)
    nout = div(nin * nin - nin, 2) #length of the output vector
    dists = Vector{eltype(v)}(undef,nout) #preallocating output vector
    k = 1 #current position in the output vector
    for i in 1:(nin-1)
        a = v[i]
        for j in (i+1):nin
            b = v[j]
            dists[k] = abs(a-b)
            k += 1
        end
    end
    dists
end


vin = readvec(ARGS[1])
distances = distances_among_pairs_loop(vin)


# time ./pairdist.jl vec1.txt
# ./pairdist.jl vec1.txt  0.50s user 0.35s system 121% cpu 0.700 total

