### sofware installation and data source

**install MACS2:**  06/11/2015
`sudo pip -H install MACS2`  

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

### Is macs2 OK for broad peaks such as H3K27ac?
a discussion [here](https://groups.google.com/forum/#!searchin/macs-announcement/macs$20for$20broad/macs-announcement/LVkBpm-2oRM/gMT_g-DS4b0J)  
Yet another note from a user argues that MACS2 can be used for broad peak calling, but by choosing correct [arguments](https://groups.google.com/forum/#!searchin/macs-announcement/h3k27ac/macs-announcement/9_LB5EsjS_Y/nwgsPN8lR-kJ):
>While I can't speak to much of the first paragraph of your message, I wanted to let you know that when it comes to histone modification analysis, using the --call-supeaks option in the command line has proven to be a phenomenally successful way to use MACS to handle modifications (right now, I'm working on H3K4me1) which have both sharp defined peaks but also very broad "peaks" which are more like domains of H3K4me1 signals clustered together. This obviously created many situations, in part because MACS will automatically combine peaks which are separated by a distance of 10bp or less into one called peak, where artefactually broad regions were called (like 30kb peaks... yeah right!).

>So many people have argued, including in a recent review in Nat Immunology about ChIP-seq and peak-calling, that modifications with broad distribution (even H3K27Ac can be broad in our hands) should not be analyzed with MACS; using various biological end-points as testing I have found that this is not true and that MACS outperforms ZINBA (specifically designed for broad histone modifications) WHEN the subpeaks function is called for detection of histone peaks with broad, narrow, or both types of signal distribution.


It seems to me that MACS2 has evloved a lot to deal with the broad peaks compared with the widely used MACS14. Although other tools such as SICER are designed sepcifically for histone modifications, I am still going to use MACS2 for H3K27ac ChIP-seq peak calling.

###starting analysis  

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
The bedgraph file generated by macs2 is very huge (1Gb for this particular case), because it contains decimals for p-values(?). If you want to visualize it in IGV, you need to get a TDF file first. Remember to change the suffix .bdg to .bedgraph, otherwise IGV will not recoginize the file format.  

I personally like to covert the bam files directly to [bigwig](https://genome.ucsc.edu/goldenPath/help/bigWig.html) files using [deeptools](https://github.com/fidelram/deepTools). Using 10bp as a bin size, I get a bigwig file of 205Mb and you can directly load it into IGV.  
`bamCoverage -b ../data/wgEncodeSydhHistonePanc1H3k27acUcdAlnRep1.bam --normalizeTo1x 2451960000 --missingDataAsZero yes --binSize 10 -o panc1_H3k27acRep1_deeptool_normalized.bw`  

### Results  
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
