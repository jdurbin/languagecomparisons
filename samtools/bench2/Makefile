
# See sizes of these files following simlinks
# ls -Llh

binaries = cppbam

INCLUDES= -I/Users/james/tools/SeqLib -I/Users/james/tools/SeqLib/htslib 
LIBS=/Users/james/tools/SeqLib/bin/libseqlib.a /Users/james/tools/SeqLib/htslib/libhts.a /usr/lib/libbz2.dylib /usr/lib/liblzma.dylib
#CXXFLAGS=-W -Wall  -std=c++14 -DSEQAN_HAS_ZLIB=1 -DSEQAN_HAS_BZIP2=1 -O3 -DNDEBUG -DSEQAN_ENABLE_DEBUG=0 -DSEQAN_ENABLE_TESTING=0
CXXFLAGS=

cppbam: cppbam.o
	g++ cppbam.o -o cppbam $(LIBS) -lpthread -lz -lm

cppbam.o: cppbam.cpp
	g++ -c cppbam.cpp $(INCLUDES) $(CXXFLAGS)

.PHONY: clean

clean:
	rm -f $(binaries) *.o
	

HTSJ=/Users/james/toolsource/htsjdk/build/libs/htsjdk-2.18.2-25-g0cc762f-SNAPSHOT.jar
jbam:
	javac -cp $(HTSJ) jbam.java