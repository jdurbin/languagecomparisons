#include "SeqLib/BamReader.h"
#include "SeqLib/BamWriter.h"
#include "SeqLib/BWAWrapper.h"
#include <iostream>
#include <stdio.h>
#include <ctype.h>
#include <algorithm>
#include <string>

using namespace std;
using namespace SeqLib;

struct convert {
   void operator()(char& c) { c = toupper((unsigned char)c); }
};

int main(int argc,char*argv[]){
	// open the reader BAM/SAM/CRAM
	BamReader br;
	br.Open(argv[1]);
	
	//BamWriter writer;
	//writer.SetHeader(br.Header());
	//writer.Open(argv[2]);
	//writer.WriteHeader();
	
	BamRecord r;	
	int count = 0;
	while (br.GetNextRecord(r)) {
		if (r.MapQuality() > 20){			
			//std::transform(r.Qname().begin(), r.Qname().end(),r.Qname().begin(), ::toupper);
			//for_each(r.Qname().begin(),r.Qname().end(), convert());
			//writer.WriteRecord(r);
			count++;
		}
	}
	cout<<"Count: "<<count<<endl;
}

// time ./cppbam testdata/smaller.bam output/cpp.out
// real	0m47.367s
// Records out: 39059

// time ./cppbam testdata/bigger.bam output/cpp.out
// real	1m7.351s
// 1,288,355

// Count only: 
// time ./cppbam /Volumes/data/sim/jade/chr16only_jade.bam
// Count: 15,548,210
// real	0m33.010s

