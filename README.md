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
8. [Blueprint epigenome](http://dcc.blueprint-epigenome.eu/#/home)
9. [A collection of tools and papers for nucelosome positioning and TF ChIP-seq](http://generegulation.info/)

### Papers on ChIP-seq
1. [ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia](http://www.ncbi.nlm.nih.gov/pubmed/22955991) 
2. [Practical Guidelines for the Comprehensive Analysis of ChIP-seq Data](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003326)    
3. [Systematic evaluation of factors influencing ChIP-seq fidelity](http://www.nature.com/nmeth/journal/v9/n6/full/nmeth.1985.html)
4. [ChIP–seq: advantages and challenges of a maturing technology](http://www.nature.com/nrg/journal/v10/n10/abs/nrg2641.html)
5. [ChIP–seq and beyond: new and improved methodologies to detect and characterize protein–DNA interactions](http://www.nature.com/nrg/journal/v13/n12/abs/nrg3306.html) 
6. [Beyond library size: a field guide to NGS normalization](http://biorxiv.org/content/early/2014/06/19/006403)
7. [ENCODE paper portol](http://www.nature.com/encode/threads)  
8. [Enhancer discovery and characterization](http://www.nature.com/encode/threads/enhancer-discovery-and-characterization)  

    **Protocols**  
1. [A computational pipeline for comparative ChIP-seq analyses](http://www.ncbi.nlm.nih.gov/pubmed/22179591)    
2. [Identifying ChIP-seq enrichment using MACS](http://www.nature.com/nprot/journal/v7/n9/full/nprot.2012.101.html)  
3. [Spatial clustering for identification of ChIP-enriched regions (SICER) to map regions of histone methylation patterns in embryonic stem cells](http://www.ncbi.nlm.nih.gov/pubmed/24743992)
4. [ENCODE tutorials](http://www.genome.gov/27553900) 
5. [A User's Guide to the Encyclopedia of DNA Elements (ENCODE)](http://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.1001046)  

### Peak calling  

Be careful with the peaks you get:  
[Active promoters give rise to false positive ‘Phantom Peaks’ in ChIP-seq experiments](http://nar.oxfordjournals.org/content/early/2015/06/27/nar.gkv637.long)    

It is good to have controls for your ChIP-seq experiments. A DNA input control (no antibody is applied) is prefered.
The IgG control is also fine, but because so little DNA is there, you might get many duplicated reads due to PCR artifact.

**For cancer cells, an input control can be used to correct for copy-number bias.**


[A quote from Tao Liu:](https://groups.google.com/forum/#!searchin/macs-announcement/h3k27ac/macs-announcement/9_LB5EsjS_Y/nwgsPN8lR-kJ) who develped MACS1/2

>I remember in a PloS One paper last year by Elizabeth G. Wilbanks et al.,  authors pointed out the best way to sort results in MACS is by -10*log10(pvalue) then fold enrichment. I agree with them. You don't have to worry about FDR too much if your input data are far more than ChIP data. MACS1.4 calculates FDR by swapping samples, so if your input signal has some strong bias somewhere in the genome, your FDR result would be bad. Bad FDR may mean something but it's just secondary.

1. The most popular peak caller by Tao Liu: [MACS2](https://github.com/taoliu/MACS/). Now `--broad` flag supports broad peaks calling as well.

2. [TF ChIP-seq peak calling using the Irreproducibility Discovery Rate (IDR) framework](https://sites.google.com/site/anshulkundaje/projects/idr) and many [Software Tools Used to Create the ENCODE Resource](https://genome.ucsc.edu/ENCODE/encodeTools.html)    
3. [SICER](http://home.gwu.edu/~wpeng/Software.htm) for broad histone modification ChIP-seq
4. [HOMER](http://homer.salk.edu/homer/ngs/peaks.html) can also used to call Transcription factor ChIP-seq peaks and histone 
    modification ChIP-seq peaks.
5. [MUSIC](https://github.com/gersteinlab/MUSIC)
6. [permseq](https://github.com/keleslab/permseq)  R package for mapping protein-DNA interactions in highly repetitive regions of the genomes with prior-enhanced read mapping. [Paper](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC4618727/pdf/pcbi.1004491.pdf) on PLos Comp.
7. [Ritornello](http://www.biorxiv.org/content/early/2015/12/11/034090): High fidelity control-free chip-seq peak calling. No input is required!
8. Tumor samples are heterogeneous containing different cell types. [MixChIP: a probabilistic method for cell type specific protein-DNA binding analysis](http://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-015-0834-3)  

**Different parameters using the same program can produce drastic different sets of peaks especially for histone modifications with variable enrichment length and gaps between peaks. One needs to make a valid argument for parameters he uses**  

An example of different parameters for homer `findPeaks`:  
![](./images/variablePeaks.png)


### Binding does not infer functionality  

* [A significant proportion of transcription-factor binding sites may be nonfunctional](http://judgestarling.tumblr.com/post/64874995999/hypotheses-about-the-functionality-of) A post from Judge Starling  

* Several papers have shown that changes of adjacent TF binding poorly correlates with gene expression change:
[Extensive Divergence of Transcription Factor Binding in Drosophila Embryos with Highly Conserved Gene Expression](http://www.plosgenetics.org/article/info%3Adoi%2F10.1371%2Fjournal.pgen.1003748)  
[Transcription Factors Bind Thousands of Active and Inactive Regions in theDrosophila Blastoderm](http://www.plosbiology.org/article/info%3Adoi%2F10.1371%2Fjournal.pbio.0060027)    

[The Functional Consequences of Variation in Transcription Factor Binding](http://arxiv.org/abs/1310.5166)  
>" On average, 14.7% of genes bound by a factor were differentially expressed following the knockdown of that factor, suggesting that most interactions between TF and chromatin do not result in measurable changes in gene expression levels of putative target genes. "

* paper [A large portion of the ChIP-seq signal does not correspond to true binding](http://www.ncbi.nlm.nih.gov/pubmed/26388941?dopt=Abstract&utm_source=dlvr.it&utm_medium=twitter)
* [BIDCHIPS: Bias-Decomposition of ChIP-seq Signals](http://www.perkinslab.ca/Software.html)  
	**mappability, GC-content and chromatin accessibility** affect ChIP-seq read counts. 
* [ChIP bias as a function of cross-linking time](http://link.springer.com/article/10.1007%2Fs10577-015-9509-1)   

>We analyzed the dependence of the ChIP signal on the duration of formaldehyde cross-linking time for two proteins: DNA topoisomerase 1 (Top1) that is functionally associated with the double helix in vivo, especially with active chromatin, and green fluorescent protein (GFP) that has no known bona fide interactions with DNA. With short time of formaldehyde fixation, only Top1 immunoprecipation efficiently recovered DNA from active promoters, whereas prolonged fixation augmented non-specific recovery of GFP dramatizing the need to optimize ChIP protocols to minimize the time of cross-linking, especially for abundant nuclear proteins. Thus, ChIP is a powerful approach to study the localization of protein on the genome when care is taken to manage potential artifacts.


### Gene set enrichment analysis for ChIP-seq peaks  
1. [Broad Enrich](http://broad-enrich.med.umich.edu/)  
2. [ChIP Enrich](http://chip-enrich.med.umich.edu/)  
3. [GREAT](http://bejerano.stanford.edu/great/public/html/) predicts functions of cis-regulatory regions.  
4. [ENCODE ChIP-seq significance tool](http://encodeqt.simple-encode.org/). Given a list of genes, co-regulating TFs will be identified.  
5. [cscan](http://159.149.160.51/cscan/) similar to the ENCODE significance tool.  
6. [CompGO: an R package for comparing and visualizing Gene Ontology enrichment differences between DNA binding experiments](http://www.biomedcentral.com/1471-2105/16/275)  
7. [interactive and collaborative HTML5 gene list enrichment analysis tool](http://amp.pharm.mssm.edu/Enrichr/)
8. [GeNets](http://www.broadinstitute.org/genets#computations) from Broad. Looks very promising.


### Chromatin state Segmentation  
1. [ChromHMM](http://compbio.mit.edu/ChromHMM/)  from Manolis Kellis in MIT.
  >In ChromHMM the raw reads are assigned to non-overlapping bins of 200 bps and a sample-specific threshold is used to transform the count data to binary values

2. [Segway](https://www.pmgenomics.ca/hoffmanlab/proj/segway/) from Hoffman lab. Base pair resolution. Takes longer time to run.  
3. [epicseg](https://github.com/lamortenera/epicseg) published 2015 in genome biology. Similiar speed with ChromHMM.   
4. [Spectacle: fast chromatin state annotation using spectral learning](https://github.com/jiminsong/Spectacle). Also published 2015 in genome biology.  

### Peak annotation 

1. Homer [`annotatePeak`](http://homer.salk.edu/homer/ngs/annotation.html) 
2. Bioconductor package [ChIPseeker](http://bioconductor.org/packages/release/bioc/html/ChIPseeker.html) by [Guangchuan Yu](http://ygc.name/)   
   See an important post by him on 0 or 1 based [coordinates](http://ygc.name/2015/08/07/parsing-bed-coordinates/).
 
 >Most of the software for ChIP annotation doesn't considered this issue when annotating peak (0-based) to transcript (1-based). To my knowledge, only HOMER consider this issue. After I figure this out, I have updated ChIPseeker (version >= 1.4.3) to fix the issue.
 
3. Bioconductor package [ChIPpeakAnno](http://bioconductor.org/packages/release/bioc/html/ChIPpeakAnno.html). There is a bug with this package, not sure if it is solved or not. Still a post from Guangchuan Yu: [Bug of R package ChIPpeakAnno](http://ygc.name/2014/01/14/bug-of-r-package-chippeakanno/). 

 >I used R package ChIPpeakAnno for annotating peaks, and found that it handle  the DNA strand in the wrong way. Maybe the developers were from the computer science but not biology background.

There are many other tools, I just listed three. 

* [DNAshapeR predicts DNA shape features in an ultra-fast, high-throughput manner from genomic sequencing data](http://tsupeichiu.github.io/DNAshapeR/)  

### Differential peak detection  
Look at a [post](http://andre-rendeiro.me/2015/04/03/chipseq_diffbind_analysis/) and [here](http://crazyhottommy.blogspot.com/2013/10/compare-chip-seq-data-for-different.html) describing different tools.  

1. [MultiGPS](http://mahonylab.org/software/multigps/)  

2. [PePr](https://github.com/shawnzhangyx/PePr). It can also call peaks.  

3. [histoneHMM](http://histonehmm.molgen.mpg.de/)  

4. [diffreps](https://github.com/shenlab-sinai/diffreps) for histone.  developed by Shen Li's lab in Mount Sinai who also develped [ngs.plot](https://github.com/shenlab-sinai/ngsplot).  

5. [diffbind bioconductor package](http://bioconductor.org/packages/release/bioc/html/DiffBind.html). Internally uses RNA-seq tools: EdgR or DESeq.  Most likely, I will use this tool.  

6. [ChIPComp](http://web1.sph.emory.edu/users/hwu30/software/ChIPComp.html). Very little tutorial. Now it is on bioconductor.

7. [csaw bioconductor package](http://bioconductor.org/packages/release/bioc/html/csaw.html). Tutorial [here](https://www.bioconductor.org/help/course-materials/2015/BioC2015/csaw_lab.html)  

8. [chromDiff](http://compbio.mit.edu/ChromDiff/Download.html). Also from from Manolis Kellis in MIT. Similar with ChromHMM, documentation is not that detailed. Will have a try on this.  
9. [MACS2 can detect differential peaks as well](https://github.com/taoliu/MACS/wiki/Call-differential-binding-events)  
10. paper [Identifying differential transcription factor binding in ChIP-seq](http://journal.frontiersin.org/article/10.3389/fgene.2015.00169/full)  


### Motif enrichment
1. [HOMER](http://homer.salk.edu/homer/ngs/peakMotifs.html). It has really detailed documentation. It can also be used to call peaks.   
suggestions for finding motifs from histone modification ChIP-seq data from HOMER page:
>Since you are looking at a region, you do not necessarily want to center the peak on the specific position with the highest tag density, which may be at the edge of the region.  Besides, in the case of histone modifications at enhancers, the highest signal will usually be found on nucleosomes surrounding the center of the enhancer, which is where the functional sequences and transcription factor binding sites reside.  Consider H3K4me marks surrounding distal PU.1 transcription factor peaks.  Typically, adding the -center option moves peaks further away from the functional sequence in these scenarios.

2. [MEME suite](http://meme.ebi.edu.au/meme/index.html). It is probably the most popular motif finding tool in the papers.
3. [JASPAR database](http://jaspar.binf.ku.dk/  )
3. [pScan-ChIP](http://159.149.160.51/pscan_chip_dev/)  
4. [MotifMap](http://motifmap.ics.uci.edu/#MotifSearch)  
5. [RAST](http://rsat01.biologie.ens.fr/rsa-tools/index.html) Regulatory Sequence Analysis Tools.  
6. [ENCODE TF motif database](http://compbio.mit.edu/encode-motifs/)  
7. [oPOSSUM](http://opossum.cisreg.ca/oPOSSUM3/) is a web-based system for the detection of over-represented conserved transcription factor binding sites and binding site combinations in sets of genes or sequences.  
8.  my post [how to get a genome-wide motif bed file](http://crazyhottommy.blogspot.com/2014/02/how-to-get-genome-wide-motif-bed-file.html) 
9.  Many other tools [here](http://omictools.com/motif-discovery-c84-p1.html)
10. [A review of ensemble methods for de novo motif discovery in ChIP-Seq data](http://bib.oxfordjournals.org/content/early/2015/04/17/bib.bbv022.abstract)  
11. [melina2](http://melina2.hgc.jp/public/index.html). If you only have one sequence and want to know what TFs might bind
    there, this is a very useful tool.
12. [STEME](https://pypi.python.org/pypi/STEME/). A python library for motif analysis. STEME started life as an approximation to the Expectation-Maximisation algorithm for the type of model used in motif finders such as MEME. **STEME’s EM approximation runs an order of magnitude more quickly than the MEME implementation for typical parameter settings**. STEME has now developed into a fully-fledged motif finder in its own right.  
13. [CENTIPEDE: Transcription factor footprinting and binding site prediction](http://centipede.uchicago.edu/). [Tutorial](https://github.com/slowkow/CENTIPEDE.tutorial)  
14. [msCentipede: Modeling Heterogeneity across Genomic Sites and Replicates Improves Accuracy in the Inference of Transcription Factor Binding](http://rajanil.github.io/msCentipede/)  
15. [DiffLogo: A comparative visualisation of sequence motifs](http://bioconductor.org/packages/release/bioc/html/DiffLogo.html) 
16. [Weeder (version: 2.0)](http://159.149.160.51/modtools/)

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
[bigwig-python](https://github.com/brentp/bw-python)  
[samtools](http://www.htslib.org/)    
[bedtools](http://bedtools.readthedocs.org/en/latest/) my all-time favorite tool from Araon Quinlan' lab. Great documentation!   
[Hosting bigWig for UCSC visualization](http://crazyhottommy.blogspot.com/2014/02/hosting-bigwig-by-dropbox-for-ucsc.html)  
[My first play with GRO-seq data, from sam to bedgraph for visualization](http://crazyhottommy.blogspot.com/2013/10/my-first-play-with-gro-seq-data-from.html)  
[convert bam file to bigwig file and visualize in UCSC genome browser in a Box (GBiB)](http://crazyhottommy.blogspot.com/2014/10/convert-bam-file-to-bigwig-file-and.html)  



### Peaks overlapping significance test
[The genomic association tester (GAT)](https://github.com/AndreasHeger/gat)  
[poverlap](https://github.com/brentp/poverlap) from Brent Pedersen. Now he is working with Aaron Quinlan at university of Utah.  
[Genometric Correlation (GenometriCorr): an R package for spatial correlation of genome-wide interval datasets](http://genometricorr.sourceforge.net/)  
[Location overlap analysis for enrichment of genomic ranges](http://bioconductor.org/packages/release/bioc/html/LOLA.html) bioconductor package.   
[regioneR](http://bioconductor.org/packages/release/bioc/html/regioneR.html) Association analysis of genomic regions based on permutation tests
[similaRpeak](http://bioconductor.org/packages/devel/bioc/html/similaRpeak.html): Metrics to estimate a level of similarity between two ChIP-Seq profiles

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
4. [ChAsE](http://www.epigenomes.ca/tools.html)

**One cavet is that the meta-plot (on the left) is an average view of ChIP-seq
tag enrichment and may not reflect the real biological meaning for individual cases.**  

See a post from Lior Patcher [How to average genome-wide data](How to average genome-wide data)  

I replied the post:
>for ChIP-seq, in addition to the average plot, a heatmap that with each region in each row should make it more clear to compare (although not quantitatively). a box-plot (or a histogram) is better in this case . I am really uncomfortable averaging the signal, as a single value (mean) is not a good description of the distribution.

By Meromit Singer:  
>thanks for the paper ref! Indeed, an additional important issue with averaging is that one could be looking at the aggregation of several (possibly very distinct) clusters. Another thing we should all keep in mind if we choose to make such plots..

A paper from Genome Research [Ubiquitous heterogeneity and asymmetry of the chromatin environment at regulatory elements](http://m.genome.cshlp.org/content/22/9/1735.full)

### Enhancer databases
* [FANTOM project](http://fantom.gsc.riken.jp/5/)  CAGE for promoters and enhancers.
* [DENdb: database of integrated human enhancers](http://www.cbrc.kaust.edu.sa/dendb/)  
* [VISTA enhancer browser](http://enhancer.lbl.gov/)  
* [Super-enhancer database](http://www.bio-bigdata.com/SEA/)

### Enhancer target prediction 

* [Assessing Computational Methods for Transcription Factor Target Gene Identification Based on ChIP-seq Data](http://www.ploscompbiol.org/article/info:doi/10.1371/journal.pcbi.1003342#pcbi.1003342.s019) 
* [Protein binding and methylation on looping chromatin accurately predict distal regulatory interactions](http://biorxiv.org/content/early/2015/07/09/022293)
* [i-cisTarget](http://gbiomed.kuleuven.be/apps/lcb/i-cisTarget/)
* [protocol iRegulon and i-cisTarget: Reconstructing Regulatory Networks Using Motif and Track Enrichment](http://www.ncbi.nlm.nih.gov/pubmed/26678384?dopt=Abstract&utm_source=dlvr.it&utm_medium=twitter)  
* [Model-based Analysis of Regulation of Gene Expression](http://cistrome.org/MARGE/) from Shirley Liu's lab.

### Allele-specific analysis  
* [WASP: allele-specific software for robust molecular quantitative trait locus discovery](http://www.nature.com/nmeth/journal/vaop/ncurrent/full/nmeth.3582.html)
* [ABC -- (Allele-specific Binding from ChIP-Seq)](https://github.com/mlupien/ABC/)

### SNPs affect on TF binding
* [RegulomeDB](http://www.regulomedb.org/)  Use RegulomeDB to identify DNA features and regulatory elements in non-coding regions of the human genome by entering dbSNP id, chromosome regions or single Nucleotides.  
* [motifbreakR](http://bioconductor.org/packages/devel/bioc/html/motifbreakR.html) A Package For Predicting The Disruptiveness Of Single Nucleotide Polymorphisms On Transcription Factor Binding Sites.
* [GERV: A Statistical Method for Generative Evaluation of Regulatory Variants for Transcription Factor Binding](http://www.ncbi.nlm.nih.gov/pubmed/26476779?dopt=Abstract&utm_source=dlvr.it&utm_medium=twitter) From the same group as above.
* [PRIME: Predicted Regulatory Impact of a Mutation in an Enhancer](https://github.com/aertslab/primescore)  

### co-occurring TFs

* In-silico Search for co-occuring transcription factors: [INSECT](http://bioinformatics.ibioba-mpsp-conicet.gov.ar:84/INSECT/index.html) 
* [INSECT 2](http://bioinformatics.ibioba-mpsp-conicet.gov.ar/INSECT2/)
* CO-factors associated with Uniquely-bound GEnomic Regions:[COUGER](http://couger.oit.duke.edu/)  
* 

### Conservation of the peak underlying DNA sequences
* [bioconductor annotation package phastCons100way.UCSC.hg19](https://bioconductor.org/packages/release/data/annotation/html/phastCons100way.UCSC.hg19.html)
* 


### Integration of different data sets

[methylPipe and compEpiTools: a suite of R packages for the integrative analysis of epigenomics data](http://www.ncbi.nlm.nih.gov/pubmed/26415965?dopt=Abstract&utm_source=dlvr.it&utm_medium=twitter)  

[Copy number information from targeted sequencing using off-target reads](https://bioconductor.org/packages/release/bioc/html/CopywriteR.html) bioconductor CopywriteR package.   

[3CPET](http://www.bioconductor.org/packages/release/bioc/html/R3CPET.html): Finding Co-factor Complexes in Chia-PET experiment using a Hierarchical Dirichlet Process


### ATAC-seq
* [RASQUAL](https://github.com/dg13/rasqual) (Robust Allele Specific QUAntification and quality controL) maps QTLs for sequenced based cellular traits by combining population and allele-specific signals. [paper: Fine-mapping cellular QTLs with RASQUAL and ATAC-seq](http://www.nature.com/ng/journal/vaop/ncurrent/full/ng.3467.html) 
* [ATAC-seq Forum](https://sites.google.com/site/atacseqpublic/home?pli=1)  
* [Single-cell ATAC-Seq](http://cole-trapnell-lab.github.io/projects/sc-atac/)  
* [Global Prediction of Chromatin Accessibility Using RNA-seq from Small Number of Cells](http://www.biorxiv.org/content/early/2016/01/01/035816)  from RNA-seq to DNA accessibility. [tool on github](https://github.com/WeiqiangZhou/BIRD)  
* 

### DNase-seq
* [pyDNase](https://github.com/jpiper/pyDNase) - a library for analyzing DNase-seq data. [paper: Wellington-bootstrap: differential DNase-seq footprinting identifies cell-type determining transcription factors](http://bmcgenomics.biomedcentral.com/articles/10.1186/s12864-015-2081-4)  
* 
