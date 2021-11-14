#!/usr/bin/env julia

using XAM,Plots

bamName = ARGS[1]
plotName = ARGS[2]

function histQuals(bamInName)    
    allquals=[]
	print("Reading BAM...")
    bamIn = open(BAM.Reader,bamInName)
    for a in bamIn
        push!(allquals,BAM.mappingquality(a))
    end
	println("done.")
	#print(Int.(allquals[1:100])) # Int. bit is so output is shown as ints not as hex
	
    histogram(allquals)
end


hist = histQuals(bamName)
print("Saving fig to ",plotName,"...")
savefig(hist,plotName)
println("done.")


# time ./qualhist.jl data/PC-HLA-EG4.bam histjl.png
# Reading BAM...done.
# Saving fig to histjl.png...done.
# 
# 14.32s user 0.78s system 99% cpu 15.241 total


# time qualhist.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam histjl.png
# Reading BAM...done.
# Saving fig to histjl.png...done.
# qualhist.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam histjl.png  
# 29.42s user 1.53s system 99% cpu 31.158 total

# This implies:
# Warmup time 13.95 sec .
# Time to complete after warmup: 15.05 sec
