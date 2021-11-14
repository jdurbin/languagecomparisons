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

		final SamReader reader = SamReaderFactory.makeDefault()
			.validationStringency(ValidationStringency.SILENT)
			.open(new File(bamFileName));

		int count = 0;
		for (final SAMRecord align : reader) {
			if (align.getMappingQuality() > 20){
				align.setReadName(align.getReadName().toUpperCase())
			}
		}		
	}
}

