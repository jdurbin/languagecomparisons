#!/usr/bin/env julia

using XAM

reader = open(BAM.Reader, "testdata/c6_40X_HG002.bam")
record = BAM.Record()

count=0
while !eof(reader)
	empty!(record)
	read!(reader, record)
	
	if BAM.mappingquality(record) > 20
		global count += 1
	end
end

println(count)


# time ./juliabam2.jl
# 42950015
# ./juliabam2.jl  61.56s user 1.76s system 99% cpu 1:03.36 total