#include "SeqLib/BamReader.h"
#include "SeqLib/BamWriter.h"
#include "SeqLib/BWAWrapper.h"
#include <iostream>
using namespace std;
using namespace SeqLib;

int main(int argc,char*argv[]){

	// open the reader BAM/SAM/CRAM
	BamReader br;
	br.Open(argv[1]);
	
	BamRecord r;	
	int count = 0;
	while (br.GetNextRecord(r)) {
		if (r.MapQuality() > 20){
			count++;
			//cout<<r.Qname()<<"\t"<<r.Length()<<"\n";
		}
	}
	cout<<"Count: "<<count<<endl;
}

