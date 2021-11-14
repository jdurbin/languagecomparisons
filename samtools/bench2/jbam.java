import htsjdk.samtools.DefaultSAMRecordFactory;
import htsjdk.samtools.SAMFileWriter;
import htsjdk.samtools.SAMFileWriterFactory;
import htsjdk.samtools.SAMRecord;
import htsjdk.samtools.SamInputResource;
import htsjdk.samtools.SamReader;
import htsjdk.samtools.SamReaderFactory;
import htsjdk.samtools.ValidationStringency;
import htsjdk.samtools.seekablestream.SeekableStream;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.net.URL;

public class jbam{

	public static void main(String[] args){

		String bamFileName = args[0];
		try{
			final SamReader reader = SamReaderFactory.makeDefault()
				.validationStringency(ValidationStringency.SILENT)
				.open(new File(bamFileName));
				
			File outBamFile = new File(args[1]);
			final SAMFileWriter outputSam = new SAMFileWriterFactory().
											makeSAMOrBAMWriter(reader.getFileHeader(),
			                				true, outBamFile);
	
			int count = 0;
			for (final SAMRecord align : reader) {
				if (align.getMappingQuality() > 20){
					align.setReadName(align.getReadName().toUpperCase());
					outputSam.addAlignment(align);
				}
			}
			outputSam.close();
			reader.close();
		}catch(Exception e){
			System.err.println("Some kind of exception");			
		}		
	}
}

// time java jbam testdata/smaller.bam output/jsm.bam
// real	0m50.321s