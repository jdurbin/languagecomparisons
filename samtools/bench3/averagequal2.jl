#!/usr/bin/env julia

using XAM,Statistics

bamName = ARGS[1]

function histQuals(bamInName)    
    allquals=Int[]
	print("Reading BAM...")
    bamIn = open(BAM.Reader,bamInName)
    for a in bamIn
        push!(allquals,BAM.mappingquality(a))
    end
	println("done.")
	
	println("Average quality: ",mean(allquals))
end


histQuals(bamName)


# time averagequal.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam
# Reading BAM...done.
# Average quality: 43.76016208794757
# averagequal.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam  
# 15.48s user 0.94s system 99% cpu 16.422 total


# Only difference here is Int[] vs [].  The latter creates an Any array which has to 
# store pointers.  
#time averagequal2.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam
#Reading BAM...done.
#Average quality: 43.76016208794757
#averagequal2.jl /Users/james/projects/hla/capture/bam38/PC-HLA-EG4.bam  
# 14.59s user 0.76s system 100% cpu 15.304 total


# time averagequal2.jl data/PC-HLA-EG4.bam
# Reading BAM...done.
# Average quality: 56.078356406954285
# averagequal2.jl data/PC-HLA-EG4.bam  
# 1.76s user 0.31s system 103% cpu 1.999 total