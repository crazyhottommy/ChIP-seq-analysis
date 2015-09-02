### Preparing ChIP-seq count table

[Countinuing with part1](https://github.com/crazyhottommy/ChIP-seq-analysis/blob/master/part1_peak_calling.md), I've got a `merged.bed` containing the merged peaks and I will count how many reads are in those peaks using bedtools multicov and featureCounts from subRead.

#### Count by bedtools
Make a bed file adding peak id as the fourth colum.
This bed file will be used for bedtools multicov:  
`cat merge.bed | awk '{$3=$3"\t""peak_"NR}1' OFS="\t" > bed_for_multicov.bed`   

count one bam file:  
`time bedtools multicov -bams ../../data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam -bed 1000_bedtools.bed > counts_multicov.txt`  

count multiple bam files:  


Make sure the header for each bam file is identical, otherwise an error saying "Can not open bam file" will show up.  
See [here](https://groups.google.com/forum/#!msg/bedtools-discuss/_LNuoRWHn50/14MaqyzyzXsJ) and [here](https://github.com/arq5x/bedtools2/issues/52). For bam files downloaded from UCSC, some header contains chrY in the header, some do not, and the order of chrX, chrY, chrM may be different.  

change bam header:  
`samtools view -H ../../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam > bam_header.txt`  
`samtools reheader bam_header.txt ../../data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam > Mcf7H3K27acRep1_reheader.bam`  
`samtools index Mcf7H3K27acRep1_reheader.bam`  

do the same thing for other bams.  

`time bedtools multicov -bams ../../data/*bam -bed bed_for_multicov.bed > counts_bedtools.txt`  

`550.24s user 17.86s system 97% cpu 9:42.88 total`  
It is pretty fast in counting 6 bam files for a bed file containing
~40,000 entries.

The columns of counts are in the same sequences as the input bam files.

#### Count by featureCounts
Make a saf file for featureCount in the [subread package](http://bioinf.wehi.edu.au/featureCounts/)  

add peak id in the first column, add a strand info to the last column:  

`awk -F "\t" '{$1="peak_"NR FS$1;$4=$4FS"."}1' > subread.saf`  

featureCounts assumes that the default annotation file is GTF file. featureCounts is usually used to count RNAs-seq data. check the help message for other flags such as `-f`, `-t` and `-g`. use `-T` to specifiy how many threads you want to use, default is 1.  
It is a faster alternative to [htseq-count](http://www-huber.embl.de/users/anders/HTSeq/doc/count.html) which is widely used for gene-level RNA-seq counts.

`time featureCounts -a subread.saf -F SAF -o counts_subread.txt ../../data/*bam -T 4` 

`274.74s user 3.16s system 417% cpu 1:06.55 total`

**Using 4 cpus, the speed is faster than bedtools**

The output file contains two lines of header:  
the first line is the command used to generate the output; the second line
is the header composed of Geneid, Chr, Start, End, Strand, Length, and the name of 
the input bam files.  

Strand will be all "+" although the peaks do not have any strandness. 

besides the `counts_subread.txt` file, another `counts_subread.txt.summary`
file will be generated detailing how many reads are assigned or not.


#### Join the two counts table to compare the differences
Join the two counts table using the common peak id column, use `csvjoin` from [csvkit](http://csvkit.readthedocs.org/en/latest/index.html#)    

`csvjoin -t -c1,4 <(cat counts_subread.txt | sed '1,2d') counts_bedtools.txt |  cut -d"," -f1-12,17-22 > joined_counts_table.csv`   

Now, we can load the csv file into R to do some exploration. I put the exploration on [Rpubs](http://rpubs.com/crazyhottommy/ChIP-seq-counts). 




