# ChIP-seq-analysis

### Resources for ChIP-seq data 
1. [ENCODE: Encyclopedia of DNA Elements](https://www.encodeproject.org/)  
2. [ENCODE Factorbook](https://www.encodeproject.org/)  
3. [ChromNet ChIP-seq interactions](http://chromnet.cs.washington.edu/#/?search=&threshold=0.5)  
    paper: [Learning the human chromatin network using all ENCODE ChIP-seq datasets](http://biorxiv.org/content/early/2015/08/04/023911)  
4. [The International Human Epigenome Consortium (IHEC) epigenome data portal](http://epigenomesportal.ca/ihec/index.html?as=1)
5. [GEO](http://www.ncbi.nlm.nih.gov/gds/?term=). Sequences are in .sra format, need to use sratools to dump into fastq.
6. [European Nucleotide Archive](http://www.ebi.ac.uk/ena). Sequences are available in fastq format.
7. [Data bases and software from Sheirly Liu's lab at Harvard](http://liulab.dfci.harvard.edu/WEBSITE/software.htm) 

### Papers on ChIP-seq
1. [ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia](http://www.ncbi.nlm.nih.gov/pubmed/22955991) 
2. [Practical Guidelines for the Comprehensive Analysis of ChIP-seq Data](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003326)    
3. [Systematic evaluation of factors influencing ChIP-seq fidelity](http://www.nature.com/nmeth/journal/v9/n6/full/nmeth.1985.html)
4. [ChIP–seq: advantages and challenges of a maturing technology](http://www.nature.com/nrg/journal/v10/n10/abs/nrg2641.html)
5. [ChIP–seq and beyond: new and improved methodologies to detect and characterize protein–DNA interactions](http://www.nature.com/nrg/journal/v13/n12/abs/nrg3306.html)  

    **Protocols**  
1. [A computational pipeline for comparative ChIP-seq analyses](http://www.ncbi.nlm.nih.gov/pubmed/22179591)    
2. [Identifying ChIP-seq enrichment using MACS](http://www.nature.com/nprot/journal/v7/n9/full/nprot.2012.101.html)  
3. [Spatial clustering for identification of ChIP-enriched regions (SICER) to map regions of histone methylation patterns in embryonic stem cells](http://www.ncbi.nlm.nih.gov/pubmed/24743992)
4. [ENCODE tutorials](http://www.genome.gov/27553900)  

### Peak calling  
1. The most popular peak caller by Tao Liu: [MACS2](https://github.com/taoliu/MACS/). Now `--broad` flag supports broad peaks calling as well.  
2. [SICER](http://home.gwu.edu/~wpeng/Software.htm) for broad histone modification ChIP-seq
3. [HOMER](http://homer.salk.edu/homer/ngs/peaks.html) can also used to call Transcription factor ChIP-seq peaks and histone 
    modification ChIP-seq peaks.
**Different parameters using the same program can produce drastic different sets of peaks especially for histone modifications with variable enrichment length and gaps between peaks. One needs to make a valid argument for parameters he uses**  

An example of different parameters for homer `findPeaks`:  
![](./images/variablePeaks.png)

### Gene set enrichment analysis for ChIP-seq peaks  
1. [Broad Enrich](http://broad-enrich.med.umich.edu/)  
2. [ChIP Enrich](http://chip-enrich.med.umich.edu/)  
3. [GREAT](http://bejerano.stanford.edu/great/public/html/) predicts functions of cis-regulatory regions.  
4. [ENCODE ChIP-seq significance tool](http://encodeqt.simple-encode.org/). Given a list of genes, co-regulated TFs will be identified.  
5. [cscan](http://159.149.160.51/cscan/) similar to the ENCODE significance tool.  


### Chromatin state Segmentation  
1. [ChromHMM](http://compbio.mit.edu/ChromHMM/)  from Manolis Kellis in MIT.
  >In ChromHMM the raw reads are assigned to non-overlapping bins of 200 bps and a sample-specific threshold is used to transform the count data to binary values

2. [Segway](https://www.pmgenomics.ca/hoffmanlab/proj/segway/) from Hoffman lab. Base pair resolution. Takes longer time to run.  
3. [epicseg](https://github.com/lamortenera/epicseg) published 2015 in genome biology. Similiar speed with ChromHMM.   
4. [Spectacle: fast chromatin state annotation using spectral learning](https://github.com/jiminsong/Spectacle). Also published 2015 in genome biology.  

### Peak annotation 

1. Homer [`annotatePeak`](http://homer.salk.edu/homer/ngs/annotation.html) 
2. Bioconductor package [ChIPseeker](http://bioconductor.org/packages/release/bioc/html/ChIPseeker.html) by [Guangchuan Yu](http://ygc.name/)   
   See an important post by him on 0 or 1 based [cooridnates](http://ygc.name/2015/08/07/parsing-bed-coordinates/).
 
 >Most of the software for ChIP annotation doesn't considered this issue when annotating peak (0-based) to transcript (1-based). To my knowledge, only HOMER consider this issue. After I figure this out, I have updated ChIPseeker (version >= 1.4.3) to fix the issue.
 
3. Bioconductor package [ChIPpeakAnno](http://bioconductor.org/packages/release/bioc/html/ChIPpeakAnno.html). There is a bug with this package, not sure if it is solved or not. Still a post from Guangchuan Yu: [Bug of R package ChIPpeakAnno](http://ygc.name/2014/01/14/bug-of-r-package-chippeakanno/). 

 >I used R package ChIPpeakAnno for annotating peaks, and found that it handle  the DNA strand in the wrong way. Maybe the developers were from the computer science but not biology background.

There are many other tools, I just listed three. 

   
    
### Differential peak detection  
Look at a [post](http://andre-rendeiro.me/2015/04/03/chipseq_diffbind_analysis/) here describing different tools.   
1. [MultiGPS](http://mahonylab.org/software/multigps/)  
2. [PePr](https://github.com/shawnzhangyx/PePr). It can also call peaks.  
3. [histoneHMM](http://histonehmm.molgen.mpg.de/)  
4. [diffreps](https://github.com/shenlab-sinai/diffreps) for histone.  developed by Shen Li's lab in Mount Sinai who also develped [ngs.plot](https://github.com/shenlab-sinai/ngsplot).  
5. [diffbind bioconductor package](http://bioconductor.org/packages/release/bioc/html/DiffBind.html). Internally uses RNA-seq tools: EdgR or DESeq.  Most likely, I will use this tool.  
6. [ChIPComp](http://web1.sph.emory.edu/users/hwu30/software/ChIPComp.html). Very little tutorial.  
7. [csaw bioconductor package](http://bioconductor.org/packages/release/bioc/html/csaw.html)  
8. [chromDiff](http://compbio.mit.edu/ChromDiff/Download.html). Also from from Manolis Kellis in MIT. Similar with ChromHMM, documentation is not that detailed. Will have a try on this.  


### Motif enrichment
1. [HOMER](http://homer.salk.edu/homer/ngs/peakMotifs.html). It has really detailed documentation. It can also be used to call peaks.   
suggestions for finding motifs from histone modification ChIP-seq data from HOMER page:
>Since you are looking at a region, you do not necessarily want to center the peak on the specific position with the highest tag density, which may be at the edge of the region.  Besides, in the case of histone modifications at enhancers, the highest signal will usually be found on nucleosomes surrounding the center of the enhancer, which is where the functional sequences and transcription factor binding sites reside.  Consider H3K4me marks surrounding distal PU.1 transcription factor peaks.  Typically, adding the -center option moves peaks further away from the functional sequence in these scenarios.

2. [MEME suite](http://meme.ebi.edu.au/meme/index.html). It is probably the most popular motif finding tool in the papers.  
3. [pScan-ChIP](http://159.149.160.51/pscan_chip_dev/)  
4. [MotifMap](http://motifmap.ics.uci.edu/#MotifSearch)  
5. [RAST](http://rsat01.biologie.ens.fr/rsa-tools/index.html) Regulatory Sequence Analysis Tools.  
6. [ENCODE TF motif database](http://compbio.mit.edu/encode-motifs/)  
7. [oPOSSUM](http://opossum.cisreg.ca/oPOSSUM3/) is a web-based system for the detection of over-represented conserved transcription factor binding sites and binding site combinations in sets of genes or sequences.  
8.  my post [how to get a genome-wide motif bed file](http://crazyhottommy.blogspot.com/2014/02/how-to-get-genome-wide-motif-bed-file.html) 
9.  Many other tools [here](http://omictools.com/motif-discovery-c84-p1.html)  

### Super-enhancer identification   

The fancy "supper-enhancer" term was first introduced by [Richard Young](http://younglab.wi.mit.edu/publications.htm) in Whitehead Institute. Basically, super-enhancers are enhancers that span large genomic regions(~12.5kb). The concept of super-enhancer is not new. One of the most famous example is the Locus Control Region (LCR) that controls the globin gene expression, and this has been known for decades.  

A review in Nature Genetics [What are super-enhancers?](http://www.nature.com/ng/journal/v47/n1/full/ng.3167.html)


From the [HOMER page](http://homer.salk.edu/homer/ngs/peaks.html)
**How finding super enhancers works:**

>Super enhancer discovery in HOMER emulates the original strategy used by the Young lab.  First, peaks are found just like any other ChIP-Seq data set.  Then, peaks found within a given distance are 'stitched' together into larger regions (by default this is set at 12.5 kb).  The super enhancer signal of each of these regions is then determined by the total normalized number reads minus the number of normalized reads in the input.  These regions are then sorted by their score, normalized to the highest score and the number of putative enhancer regions, and then super enhancers are identified as regions past the point where the slope is greater than 1.  

Example of a super enhancer plot:
![](./images/super-enhancer-plot.png)

>In the plot above, all of the peaks past 0.95 or so would be considered "super enhancers", while the one's below would be "typical" enhancers.  If the slope threshold of 1 seems arbitrary to you, well... it is!  This part is probably the 'weakest link' in the super enhancer definition.  However, the concept is still very useful.  Please keep in mind that most enhancers probably fall on a continuum between typical and super enhancer status, so don't bother fighting over the precise number of super enhancers in a given sample and instead look for useful trends in the data.

**Using ROSE from Young lab**   
[ROSE: RANK ORDERING OF SUPER-ENHANCERS](http://younglab.wi.mit.edu/super_enhancer_code.html)  


### Bedgraph, bigwig manipulation tools
[WiggleTools](https://github.com/Ensembl/WiggleTools)  
[bigwig tool](https://github.com/CRG-Barcelona/bwtool/wiki)  
[samtools](http://www.htslib.org/)    
[bedtools](http://bedtools.readthedocs.org/en/latest/) my all-time favorite tool from Araon Quinlan' lab. Great documentation!   
[Hosting bigWig for UCSC visualization](http://crazyhottommy.blogspot.com/2014/02/hosting-bigwig-by-dropbox-for-ucsc.html)  
[My first play with GRO-seq data, from sam to bedgraph for visualization](http://crazyhottommy.blogspot.com/2013/10/my-first-play-with-gro-seq-data-from.html)  
[convert bam file to bigwig file and visualize in UCSC genome browser in a Box (GBiB)](http://crazyhottommy.blogspot.com/2014/10/convert-bam-file-to-bigwig-file-and.html)  



### Peaks overlapping significance test
[The genomic association tester (GAT)](https://github.com/AndreasHeger/gat)  
[poverlap](https://github.com/brentp/poverlap) from Brent Pedersen. Now he is working with Aaron Quinlan at university of Utah.  
[Genometric Correlation (GenometriCorr): an R package for spatial correlation of genome-wide interval datasets](http://genometricorr.sourceforge.net/)  

### RNA-seq data integration
[Beta](http://cistrome.org/BETA/) from Shirley Liu's lab in Harvard.  Tao Liu's previous lab.  


### Heatmap, mata-plot 

Many papers draw meta-plot and heatmap on certain genomic regions (2kb around TSS, genebody etc) using ChIP-seq data. 

See an example from the ngs.plot:  
![](./images/meta-heatmap.png)


**Tools**  

1. [deeptools](https://github.com/fidelram/deepTools).It can do many others and have good documentation.
It can also generate the heatmaps, but I personally use [ngs.plot](https://github.com/shenlab-sinai/ngsplot) which is esy to use. (developed in Mount Sinai).  

2. you can also draw heatmaps using R. just count (using either Homer or bedtools) the ChIP-seq reads in each bin and draw with heatmap.2 function. 
[here](http://crazyhottommy.blogspot.com/2013/08/how-to-make-heatmap-based-on-chip-seq.html) and [here](http://crazyhottommy.blogspot.com/2013/04/how-to-make-tss-plot-using-rna-seq-and.html). Those are my pretty old blog posts, I now have a much better idea on how to make those graphs from scratch.

3. You can also use bioconductor [Genomation](http://www.bioconductor.org/packages/release/bioc/vignettes/genomation/inst/doc/GenomationManual-knitr.html). It is very versatile.

**One cavet is that the meta-plot (on the left) is an average view of ChIP-seq
tag enrichment and may not reflect the real biological meaning for individual cases.**  

See a post from Lior Patcher [How to average genome-wide data](How to average genome-wide data)  

I replied the post:
>for ChIP-seq, in addition to the average plot, a heatmap that with each region in each row should make it more clear to compare (although not quantitatively). a box-plot (or a histogram) is better in this case . I am really uncomfortable averaging the signal, as a single value (mean) is not a good description of the distribution.

By Meromit Singer:  
>thanks for the paper ref! Indeed, an additional important issue with averaging is that one could be looking at the aggregation of several (possibly very distinct) clusters. Another thing we should all keep in mind if we choose to make such plots..

A paper from Genome Research [Ubiquitous heterogeneity and asymmetry of the chromatin environment at regulatory elements](http://m.genome.cshlp.org/content/22/9/1735.full)


### Allele-specific analysis  


### SNPs affect on TF binding
