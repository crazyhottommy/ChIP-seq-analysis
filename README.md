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

### Peak calling  
1. The most popular peak caller by Tao Liu: [MACS2](https://github.com/taoliu/MACS/). Now `--broad` flag supports broad peaks calling as well.  
2. [SICER](http://home.gwu.edu/~wpeng/Software.htm) for broad histone modification ChIP-seq
3. [HOMER](http://homer.salk.edu/homer/ngs/peaks.html) can also used to call Transcription factor ChIP-seq peaks and histone 
    modification ChIP-seq peaks.
**Different parameters using the same program can produce drastic different sets of peaks especially for histone modifications with variable enrichment length and gaps between peaks. One needs to make a valid argument for parameters he uses**

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

### bedgraph, bigwig manipulation tools
[WiggleTools](https://github.com/Ensembl/WiggleTools)  
[bigwig tool](https://github.com/CRG-Barcelona/bwtool/wiki)  
samtools  
bedtools  
vcftools  
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
[deeptools](https://github.com/fidelram/deepTools).It can do many others and have good documentation.
It can also generate the heatmaps, but I personally use [ngs.plot](https://github.com/shenlab-sinai/ngsplot) which is esy to use. (developed in Mount Sinai).  

you can also draw heatmaps using R. just count (using either Homer or bedtools) the ChIP-seq reads in each bin and draw with heatmap.2 function. 
[here](http://crazyhottommy.blogspot.com/2013/08/how-to-make-heatmap-based-on-chip-seq.html) and [here](http://crazyhottommy.blogspot.com/2013/04/how-to-make-tss-plot-using-rna-seq-and.html). Those are my pretty old blog posts, I now have a much better idea on how to make those graphs from scratch.

You can also use bioconductor [Genomation](http://www.bioconductor.org/packages/release/bioc/vignettes/genomation/inst/doc/GenomationManual-knitr.html). It is very versatile.

### Allele-specific analysis  


### SNPs affect on TF binding
