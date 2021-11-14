#!/usr/bin/env julia

# Info found here.  
# https://biojulia.net/XAM.jl/stable/man/hts-files/

using XAM

reader = open(BAM.Reader, "testdata/c6_40X_HG002.bam")

count=0
for record in reader
	if BAM.mappingquality(record) > 20
		global count += 1
	end
end

close(reader)
println(count)

# cool enough, certain unicode works in julia...
# 2 * π


