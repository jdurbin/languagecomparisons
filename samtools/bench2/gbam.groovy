#!/usr/bin/env groovy 

import htsjdk.samtools.*

bamFileName = args[0]

reader = SamReaderFactory.makeDefault()
	.validationStringency(ValidationStringency.SILENT)
	.open(new File(bamFileName));


writer = new SAMFileWriterFactory().
			makeSAMOrBAMWriter(reader.getFileHeader(),
	        true, new File(args[1]));

for (SAMRecord align : reader) {
	if (align.getMappingQuality() > 20){
		align.setReadName(align.getReadName().toUpperCase());
		writer.addAlignment(align);
	}
}

writer.close();
reader.close();



// time ./gbam.groovy testdata/smaller.bam output/jsm.bam
// real	0m50.095s