
### sofware installation and data source

**install MACS2:**  06/11/2015
`sudo pip -H install MACS2`  
macs2 version:2.1.0.20150420 

**install NCIS to estimate the scaling factor:**  
Download the package [here](http://www.biomedcentral.com/1471-2105/13/199):  
`wget http://www.biomedcentral.com/content/supplementary/1471-2105-13-199-s2.gz`

It is a .gz file, you can open your Rstudio and install it:  
`install.packages("~/NCIS/1471-2105-13-199-s2.gz", repos = NULL, type="source")`  
For help:  
`library(NCIS); ?NCIS`

see a post here using NCIS before MACS peak calling:  
[Adding a custom normalization to MACS](http://searchvoidstar.tumblr.com/post/52594053877/adding-a-custom-normalization-to-macs).  
when use NCIS, one needs to deduplicate the reads first. see a post on the [MACS goolge group](https://groups.google.com/forum/#!searchin/macs-announcement/NCIS/macs-announcement/cGzpyez57dI/Kga4YM6ukGYJ). Then the estimated scaling factor between ChIP and input control will be feeded into MACS2 with the `--ratio` flag:  
`macs2 callpeak -t ChIP.bam -c Control.bam --broad -g hs --broad-cutoff 0.1 --ration 1.4`

#### Data source
**downloaded the data from the ENNCODE project** on 06/11/2015 
[here](http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/) for MCF7 and panc1 cells. H3k27ac ChIP-seq, duplicates for each cell line. I choose these data sets because the SYDH Histone tracks contain input DNAs. The Broad Histione tracks do not have input DNA sequenced.

**MCF7 cells**
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam.bai`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam.bai`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7H3k27acUcdPk.narrowPeak.gz`  

**input DNA**
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam.bai`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7InputUcdAlnRep2.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistoneMcf7InputUcdAlnRep2.bam.bai`

**Panc1  cells**  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam.bai`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam`
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam.bai`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1H3k27acUcdPk.narrowPeak.gz`  

**input DNA**  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam`  
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeSydhHistone/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam.bai`

#### project layout  
It is always good to organize your project. For me, the layout is like this: 

`diff_ChIP_test` is the project main folder and it contains four sub-folders:
`data`,    `doc` ,    `results` and `scripts`.
Data are downloaded into the `data` folder, scripts are in the `scripts` folder and the output from the scripts are in the `results` folder.  
Further Reading: [A Quick Guide to Organizing Computational Biology Projects](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1000424)


### Is macs2 OK for broad peaks such as H3K27ac?
a discussion [here](https://groups.google.com/forum/#!searchin/macs-announcement/macs$20for$20broad/macs-announcement/LVkBpm-2oRM/gMT_g-DS4b0J)  
Yet another note from a user argues that MACS2 can be used for broad peak calling, but by choosing correct [arguments](https://groups.google.com/forum/#!searchin/macs-announcement/h3k27ac/macs-announcement/9_LB5EsjS_Y/nwgsPN8lR-kJ):
>While I can't speak to much of the first paragraph of your message, I wanted to let you know that when it comes to histone modification analysis, using the --call-supeaks option in the command line has proven to be a phenomenally successful way to use MACS to handle modifications (right now, I'm working on H3K4me1) which have both sharp defined peaks but also very broad "peaks" which are more like domains of H3K4me1 signals clustered together. This obviously created many situations, in part because MACS will automatically combine peaks which are separated by a distance of 10bp or less into one called peak, where artefactually broad regions were called (like 30kb peaks... yeah right!).

>So many people have argued, including in a recent review in Nat Immunology about ChIP-seq and peak-calling, that modifications with broad distribution (even H3K27Ac can be broad in our hands) should not be analyzed with MACS; using various biological end-points as testing I have found that this is not true and that MACS outperforms ZINBA (specifically designed for broad histone modifications) WHEN the subpeaks function is called for detection of histone peaks with broad, narrow, or both types of signal distribution.


It seems to me that MACS2 has evloved a lot to deal with the broad peaks compared with the widely used MACS14. Although other tools such as SICER are designed sepcifically for histone modifications, I am still going to use MACS2 for H3K27ac ChIP-seq peak calling.

Further Reading:   
[Practical Guidelines for the Comprehensive Analysis of ChIP-seq Data](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003326)  
[ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia](http://www.ncbi.nlm.nih.gov/pubmed/22955991)

###starting pilot analysis  

I am going to use one single ChIP bam file and one input file to do some initial testing with different parameters of MACS2.  

```
--broad

When this flag is on, MACS will try to composite broad regions in BED12 ( a gene-model-like format ) by putting nearby highly enriched regions into a broad region with loose cutoff. The broad region is controlled by another cutoff through --broad-cutoff. The maximum length of broad region length is 4 times of d from MACS. DEFAULT: False
```
**call peaks with macs2 using --broad, building model:**
`macs2 callpeak -t ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam -c ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n panc1H3k27acRep1 --outdir panc1H3k27acRep1_with_model_broad `

**call peaks with macs2 using --broad, bypass the model:**
`macs2 callpeak -t ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam -c ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n panc1H3k27acRep1 --outdir panc1H3k27acRep1_without_model_broad --nomodel --extsize 146`

-nomodel and --extsize 146 tell MACS2 use 146bp as fragment size to pileup sequencing reads.

For model building, a
NAME_model.r is an R script in the output which you can use to produce a PDF image about the model based on your data. Load it to R by:

`$ Rscript NAME_model.r`

The model will estimate the `d`

A note from [Tao Liu](https://groups.google.com/forum/#!searchin/macs-announcement/h3k27ac/macs-announcement/9_LB5EsjS_Y/nwgsPN8lR-kJ):  
>If the d is not small ~ < 2*tag size (for those tag size < 50bp), and the model image in PDF shows clean bimodal shape, d may be good. And several bp differences on d shouldn't affect the peak detection on general transcription factor ChIP-seq much.

>However, for Pol2 or histone marks, things may be different. Pol2 is moving so it's not appropriate to say there is a fixed fragment size. I don't know the correct answer. For histone mark ChIP-seq, since they would have a underlying characteristic 147bp resolution for a nucleosome size, you can simply skip model building and use "--shiftsize 74 --nomodel" instead. Also if you want, you can try other software like SICER and NPS.


--extsize EXTSIZE     The arbitrary extension size in bp. When nomodel is
                        true, MACS will use this value as fragment size to
                        extend each read towards 3' end, then pile them up.
                        **It's exactly twice the number of obsolete SHIFTSIZE.**
                        In previous language, each read is moved 5'->3'
                        direction to middle of fragment by 1/2 d, then
                        extended to both direction with 1/2 d. This is
                        equivalent to say each read is extended towards 5'->3'
                        into a d size fragment. DEFAULT: 200. EXTSIZE and
                        SHIFT can be combined when necessary. Check SHIFT
                        option.


**call peaks with macs2 not using --broad, bypass the model, produce bedgraph file -B, and --call-summit**
`macs2 callpeak -t ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam -c ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam -g hs -q 0.01 -n panc1H3k27acRep1_regular --call-summit -B --outdir panc1H3k27acRep1_without_model_regular --nomodel --extsize 146`

**short note fom me**  
The bedgraph file generated by macs2 is very huge (1Gb for this particular case), because it contains decimals(?). If you want to visualize it in IGV, you need to get a TDF file first. Remember to change the suffix .bdg to .bedgraph, otherwise IGV will not recoginize the file format.  

I personally like to covert the bam files directly to [bigwig](https://genome.ucsc.edu/goldenPath/help/bigWig.html) files using [deeptools](https://github.com/fidelram/deepTools). Using 10bp as a bin size, I get a bigwig file of 205Mb and you can directly load it into IGV.  
`bamCoverage -b ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam --normalizeTo1x 2451960000 --missingDataAsZero yes --binSize 10 --fragmentLength 200 -o panc1_H3k27acRep1_deeptool_normalized.bw`  

`--fragmentLength 200` will extend the reads at 3' end to 200bp, which is more reasonable for ChIP-seq data. We only sequence the first (36)bp of the DNA fragment pulled down by antibodies.
see [here](https://www.biostars.org/p/49775/#158050)

### Results from pilot analysis
#### 1. peak numbers
First, let's look at how many peaks are produced by three different settings of macs2 arguments.  
1. use --broad, build model  
it produced **54223** broadpeaks.  
2. use --broad, bypass model  
it produced **66288** broadpeaks.    
3. regular peak calling will produce a summit.bed file and narrow peaks  
it produced **182569** narrowpeaks.

**using --broad definetly improve the identification of peaks(or more appropriately:enriched regions).** 
You can find the narrow peaks in the gappedPeak file:

>NAME_peaks.gappedPeak is in BED12+3 format which contains both the broad region and narrow peaks. The 5th column is 10*-log10qvalue, to be more compatible to show grey levels on UCSC browser. Tht 7th is the start of the first narrow peak in the region, and the 8th column is the end. The 9th column should be RGB color key, however, we keep 0 here to use the default color, so change it if you want. The 10th column tells how many blocks including the starting 1bp and ending 1bp of broad regions. The 11th column shows the length of each blocks, and 12th for the starts of each blocks. 13th: fold-change, 14th: -log10pvalue, 15th: -log10qvalue. The file can be loaded directly to UCSC genome browser.


The narrowPeak file downloaded from the ENCODE website contains  73953 narrow peaks.
`zcat ../data/wgEncodeSydhHistonePanc1H3k27acUcdPk.narrowPeak.gz| wc -l    
`

Take home messages for now:  
1. Using different tools to call peaks will produce different number of peaks.  
2. Using the same tool with different settings will produce different number of peaks.  
**There is no consensus to use which arguments. It depends on your data type and purpose. The bottom line is that you need to make sense of the data and find biological siginifcances from there.**

**As long as you document how you did the analysis (so that other people can reproduce your work) and can convince people you are doing it reasonably, you are fine.** 

I will stick to use these argements for all my subsequent analysis:  
`macs2 callpeak -t ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam -c ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n panc1H3k27acRep1 --outdir panc1H3k27acRep1_without_model_broad --nomodel --extsize 146`

####2. peak quality in terms of qvalues (FDR) and overlapping.  
using [bedtools](http://bedtools.readthedocs.org/en/latest/index.html) for overlapping:  

`bedtools intersect -a panc1H3k27acRep1_with_model_broad/panc1H3k27acRep1_peaks.broadPeak -b panc1H3k27acRep1_without_model_broad/panc1H3k27acRep1_peaks.broadPeak -wa | cut -f1-3 | sort | uniq | wc -l
`
   45228
   
`bedtools intersect -a panc1H3k27acRep1_with_model_broad/panc1H3k27acRep1_peaks.broadPeak -b panc1H3k27acRep1_without_model_broad/panc1H3k27acRep1_peaks.broadPeak -wb | cut -f1-3 | sort | uniq | wc -l`
   61507  
largely they are overlapped with each other.

compare with the narrowpeaks downloaded from ENCODE:  
no-model:  
`bedtools intersect -a panc1H3k27acRep1_without_model_broad/panc1H3k27acRep1_peaks.broadPeak -b ../data/wgEncodeSydhHistonePanc1H3k27acUcdPk.narrowPeak -wa | cut -f1-3 | sort | uniq | wc -l`
   35722  
   
build model     
`bedtools intersect -a panc1H3k27acRep1_with_model_broad/panc1H3k27acRep1_peaks.broadPeak -b ../data/wgEncodeSydhHistonePanc1H3k27acUcdPk.narrowPeak -wa | cut -f1-3 | sort | uniq | wc -l` 
   28943

**it seems that without model building is giving more concordant peaks compared with the ENCODE narrowpeak.**
   
#### check FDRs
columns of the broadPeak file:  
7th: fold-change, 8th: -log10pvalue, 9th: -log10qvalue  
How many peaks have a FDR of 0.01 and fold-change of 2:   
peaks with no-model building  
`cat panc1H3k27acRep1_without_model_broad/panc1H3k27acRep1_peaks.broadPeak | awk '$9 >2  && $7 >2' | wc -l`
   41136 

peaks after building model  
` cat panc1H3k27acRep1_with_model_broad/panc1H3k27acRep1_peaks.broadPeak | awk '$9 >2  && $7 >2' | wc -l`
   35487

**it seems that without model building gives more confident peaks**

I did some exploratory analysis using R and published at [Rpub](http://rpubs.com/crazyhottommy/ChIP-seq-peak-distribution)
### mannual visualization of called peaks.


### call peaks for all the samples.

#### calculate scaling factor for each ChIP bam file using NCIS library  
By default **"Larger dataset will be scaled towards smaller dataset"** for macs2, one can **call peaks with macs2 using `--ratio` flag.** 
NCIS library needs the ChIP bam and input control bam file as two arguments. I need to write a R script and excute on the command line by using `Rscript`:  
[how to get commands line arguments for R](http://stackoverflow.com/questions/2151212/how-can-i-read-command-line-parameters-from-an-r-script/2151627#2151627)

```r
## calculate the scaling factor using NCIS for ChIP-seq data
# see links https://groups.google.com/forum/#!searchin/macs-announcement/NCIS/macs-announcement/0EF4cQF09FI/2-zlu2rqfOkJ
# http://searchvoidstar.tumblr.com/post/52594053877/adding-a-custom-normalization-to-macs
# Ming Tang 06/15/2015

library(NCIS)

library(ShortRead)

options(echo=TRUE) # set to FALSE if you not  want see commands in output 
args <- commandArgs(trailingOnly = TRUE)
print(args)
# trailingOnly=TRUE means that only your arguments are returned, check:
# print(commandsArgs(trailingOnly=FALSE))

ChIP_bam<- args[1]
input_control_bam<- args[2]

# NCIS usese the Aligned Reads object from the shortRead package, however, it is recommended
# to use GenomicAignments package to read in the bam files
# ga_ChIP<- readGAlignments(ChIP_bam)
# ga_input<-readGAlignments(input_control_bam)
# However, the resulting GenomicAlignment object is not recognized by NCIS.
# I have to use the legacy readAligned function from the ShortRead package.
# it takes around 15mins to finish

ga_ChIP<- readAligned(ChIP_bam, type="BAM")
ga_input<-readAligned(input_control_bam, type="BAM")

res<- NCIS(ga_ChIP, ga_input, data.type="AlignedRead")
res
res$est
res$r.seq.depth
```
To use it, save the R script as `NCIS_scaling.r` and on terminal:  
`Rscript ChIP.bam control.bam`  
It will output the scaling factor of ChIP/control. Note that the MACS2 flag `--ratio` is also for ChIP/control.  
```
 --ratio RATIO         When set, use a custom scaling ratio of ChIP/control
                        (e.g. calculated using NCIS) for linear scaling.
                        DEFAULT: ingore
```
**scaling factor for all four samples**  

`Rscript NCIS_scaling.r ../data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam ../data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam`  
`Rscript NCIS_scaling.r ../data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam ../data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam`  
`Rscript NCIS_scaling.r ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam  ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam`  
`Rscript NCIS_scaling.r ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam  ../data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam` 



The Scaling factor and the sequencing depth ratio are all for ChIP/control

| file_name     | scaling factor| seq depth ratio |
| ------------- |:-------------:| -----:|
| Mcf7Rep1      | 1.761996      | 2.091474 |
| Mcf7Rep2      | 1.709105      | 1.917619 |
| panc1Rep1     | 0.5861799     | 1.110217 |
| panc1Rep2     | 0.5160342     | 0.8233171|

we can get a rough idea of the size of each bam file:  

`ls -sh data/*`  
`4.0K data/README.md`
`1.3G data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam`
`6.2M data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam.bai`
`1.2G data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam`
`6.1M data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam.bai`
`468K data/wgEncodeSydhHistoneMcf7H3k27acUcdPk.narrowPeak.gz`
`773M data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam`
`5.9M data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam.bai`
`718M data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam`
`6.1M data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam.bai`
`522M data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam`
`5.9M data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam.bai`
`4.4M data/wgEncodeSydhHistonePanc1H3k27acUcdPk.narrowPeak`
`678M data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam`
`6.1M data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam.bai`


**MACS2 peak calling with --ratio**  
`macs2 callpeak -t data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep1.bam -c data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n Mcf7H3k27acUcdAlnRep1_ratio --outdir results/Mcf7H3k27acUcdAlnRep1_ratio --nomodel --extsize 146 --ratio 1.761996`  
`macs2 callpeak -t data/wgEncodeSydhHistoneMcf7H3k27acUcdAlnRep2.bam -c data/wgEncodeSydhHistoneMcf7InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n Mcf7H3k27acUcdAlnRep2_ratio --outdir results/Mcf7H3k27acUcdAlnRep2_ratio --nomodel --extsize 146 --ratio 1.709105`  
`macs2 callpeak -t data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam -c data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n Panc17H3k27acUcdAlnRep1_ratio --outdir results/Panc1H3k27acUcdAlnRep1_ratio --nomodel --extsize 146 --ratio 0.5861799`  
`macs2 callpeak -t data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep2.bam -c data/wgEncodeSydhHistonePanc1InputUcdAlnRep1.bam --broad -g hs --broad-cutoff 0.1 -n Panc17H3k27acUcdAlnRep2_ratio --outdir results/Panc1H3k27acUcdAlnRep2_ratio --nomodel --extsize 146 --ratio 0.5861799`


**MACS2 peak calling without --ratio**

To bulk process the bam files downloaded from ENCODE,one can write a bash script. 

```bash
#! /bin/bash

set -e
set -u
set -o pipefail -o errexit -o nounset

# we loop for the ChIP bam files
for bam in ../data/*H3k27ac*bam
do 
	# strip out only the meaningful filename to be used for output
	file_name=$(echo "$bam" | sed -E "s/..\/data\/wg.+Histone(.+)(H3k27ac.+).bam/\1\2/")
	
	# need to retain the ../data/ path. it could be simply: sed -E "s/H3k27ac/Input/" if 
	# every bam file has a input control
	input_control=$(echo "$bam" | sed -E "s/(wg.+Histone)(.+)(H3k27ac.+).bam/\1\2InputUcdAlnRep1.bam/")
	
	echo "processing ${file_name} bam file"
	echo "the input control file is ${input_control}"
	echo "calling peaks with macs2"
	macs2 callpeak -t "$bam" -c "${input_control}"  --broad -g hs --broad-cutoff 0.1 -n "${file_name}" --outdir ../results/"${file_name}"  --nomodel --extsize 146
	
done


```

The sed regular expression caused me some headache.
for `+` operator to function in sed, one needs to turn on the `-E` flag for extended regular expression on macOS, or `-r` on GNU sed.  
To caputure part of the pattern, use \1, and the parentheses do not need to be escaped:  
If you wanted to keep the first word of a line, and delete the rest of the line:
`sed 's/\([a-z]*\).*/\1'`  
or turn on the -E flag:  
`sed -E 's/([a-z]*).*/\1'`  
see a very good tutorial on [sed](http://www.grymoire.com/Unix/Sed.html).  

After execute the bash script, 4 folders are created in the `results` folder:`Mcf7H3k27acUcdAlnRep1`,`Mcf7H3k27acUcdAlnRep2`,`Panc1H3k27acUcdAlnRep1` and `Panc1H3k27acUcdAlnRep2`


### Peak number with and without --ratio
| file_name     | with --ratio  | without --ratio | overlapping |
| ------------- |:-------------:| -----------------:|--------:|
| Mcf7Rep1      | 25744         | 18572             |  18572  |
| Mcf7Rep2      | 17564         | 12257             |  12256  |
| panc1Rep1     | 348968        | 66288             |  66282  |
| panc1Rep2     | 71033         | 54312             |  54229  |

It looks like that including the --ratio will generally increase the peak number. Especially for Pan1Rep1, it has 5 times more peaks with --ratio than without --ratio.  
It will be interesting to check the peak quality of the increasing number of peaks after adding --ratio. I mannually checked several peaks and found that the newly found peaks are mostly very weak ones. **I decided to do my subsequent analysis with the peaks got from the MACS2 without --ratio.**


### filter peaks from the blacklists
[blacklists](https://sites.google.com/site/anshulkundaje/projects/blacklists)

>Functional genomics experiments based on next-gen sequencing (e.g. ChIP-seq, MNase-seq, DNase-seq, FAIRE-seq) that measure biochemical activity of various elements in the genome often produce artifact signal in certain regions of the genome. It is important to keep track of and filter artifact regions that tend to show artificially high signal (excessive unstructured anomalous reads mapping). Below is a list of comprehensive empirical blacklists identified by the ENCODE and modENCODE consortia. Note that these blacklists were empirically derived from large compendia of data using a combination of automated heuristics and manual curation. These blacklists are applicable to functional genomic data based on short-read sequencing (20-100bp reads). These are not directly applicable to RNA-seq or any other transcriptome data types. The blacklisted regions typically appear u
niquely mappable so simple mappability filters do not remove them. These regions are often found at specific types of repeats such as centromeres, telomeres and satellite repeats. It is especially important to remove these regions that computing measures of similarity such as Pearson correlation between genome-wide tracks that are especially affected by outliers.

download the hg19 blacklist into the `data` folder by 
`wget http://hgdownload.cse.ucsc.edu/goldenPath/hg19/encodeDCC/wgEncodeMapability/wgEncodeDacMapabilityConsensusExcludable.bed.gz`

creat a new folder `broad_peaks_all` inside the `results` folder, and copy all the broad peaks to this folder.  
`  ls ./broad_peaks_all`  
`Mcf7H3k27acUcdAlnRep1_peaks.broadPeak`  `Panc1H3k27acUcdAlnRep1_peaks.broadPeak`
`Mcf7H3k27acUcdAlnRep2_peaks.broadPeak`  `Panc1H3k27acUcdAlnRep2_peaks.broadPeak`

```bash
#! /bin/bash

## filter the broad peaks from MACS output against the blacklist regions
## bedtools intersect -v

set -e
set -u
set -o pipefail -o errexit -o nounset


for peak in ../results/broad_peaks_all/*broadPeak
do
	file_name=$(basename $peak .broadPeak)
	bedtools intersect -a "$peak" -b ../data/wgEncodeDacMapabilityConsensusExcludable.bed -v \
	> ../results/broad_peaks_all/"${file_name}".filtered.bed
done
```
save the bash script as `filter_blacklist.sh` and run it at terminal in the `script` folder `./fiter_blacklist.sh`. 

```bash
chmod u+x filter_blacklist.sh
```
After filtering:  
`wc -l /broad_peaks_all/*`  
   `18572 Mcf7H3k27acUcdAlnRep1_peaks.broadPeak`
   `18548 Mcf7H3k27acUcdAlnRep1_peaks.filtered.bed`
   `12257 Mcf7H3k27acUcdAlnRep2_peaks.broadPeak`
   `12239 Mcf7H3k27acUcdAlnRep2_peaks.filtered.bed`
   `66288 Panc1H3k27acUcdAlnRep1_peaks.broadPeak`
   `66248 Panc1H3k27acUcdAlnRep1_peaks.filtered.bed`
   `54312 Panc1H3k27acUcdAlnRep2_peaks.broadPeak`
   `54235 Panc1H3k27acUcdAlnRep2_peaks.filtered.bed`  
Then remove all the broadpeaks:  
`rm *broadPeak`

### merge peaks
After get the filtered peaks, I need to merge all the peaks into a superset that contains all the peaks. I will first select out the peaks that overlap with each other between biological replicates, and then merge all four of them using bedtools.  
`bedtools intersect -a Mcf7H3k27acUcdAlnRep1_peaks.filtered.bed -b Mcf7H3k27acUcdAlnRep2_peaks.filtered.bed -wa | cut -f1-3 | sort | uniq > Mcf7Rep1_peaks.bed `  
`bedtools intersect -a Mcf7H3k27acUcdAlnRep1_peaks.filtered.bed -b Mcf7H3k27acUcdAlnRep2_peaks.filtered.bed -wb | cut -f1-3 | sort | uniq > Mcf7Rep2_peaks.bed `  
`bedtools intersect -a Panc1H3k27acUcdAlnRep1_peaks.filtered.bed -b Panc1H3k27acUcdAlnRep2_peaks.filtered.bed -wa | cut -f1-3 | sort | uniq > Panc1Rep1_peaks.bed`  
`bedtools intersect -a Panc1H3k27acUcdAlnRep1_peaks.filtered.bed -b Panc1H3k27acUcdAlnRep2_peaks.filtered.bed -wb | cut -f1-3 | sort | uniq > Panc1Rep2_peaks.bed`  

`wc -l *`  
   `18548 Mcf7H3k27acUcdAlnRep1_peaks.filtered.bed`
   `12239 Mcf7H3k27acUcdAlnRep2_peaks.filtered.bed`
    `9679 Mcf7Rep1_peaks.bed`  
   `11319 Mcf7Rep2_peaks.bed`
   `66248 Panc1H3k27acUcdAlnRep1_peaks.filtered.bed`
   `54235 Panc1H3k27acUcdAlnRep2_peaks.filtered.bed`
   `35218 Panc1Rep1_peaks.bed`  
   `44358 Panc1Rep2_peaks.bed`


`rm *filtered*`  
`cat *bed | sort -k1,1 -k2,2n | bedtools merge | tee merge.bed | wc -l`  
39046  
**we got a final superset containing 39046 peaks.**
