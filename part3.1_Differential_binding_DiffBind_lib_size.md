
### library size and normalization for ChIP-seq
I have discussed how to use DESeq2 to do differential binding for ChIP-seq at [here](https://github.com/crazyhottommy/ChIP-seq-analysis/blob/master/part3_Differential_binding_by_DESeq2.md).  
I am experimenting [`DiffBind`](http://bioconductor.org/packages/release/bioc/html/DiffBind.html) to do the same thing, which internally uses EdgR, DESeq and DESeq2.
The author `Rory Stark` is very responsive on the [bioconductor support site](https://support.bioconductor.org/) and has answered several of my questions.

Today, I am going to keep a note here for normalizing the ChIP-seq data.
If one compares ChIP-seq versus RNA-seq data, they are in the end are all counts data. For RNA-seq, we usually get a read count table for
the counts in the exons (union of them is for a gene); for ChIP-seq, we get a read count table for counts within the peaks. The peaks have to
be identified by other tools such as MACS first. The counts data follow a **(negative) binomial distribution**. That's why tools such as DESeq2, which was developed for RNAseq is used for ChIP-seq.

After we get a count table, it comes to the normalization problem. If you are interested, read this paper [Beyond library size: a field guide to NGS normalization](http://biorxiv.org/content/early/2014/06/19/006403).
In the `DiffBind` package, the counts table is obtained by a function `?dba.count`.

There are several ways to specify how the counts are normalized for the binding affinity matrix:
```
score	
which score to use in the binding affinity matrix. Note that all raw read counts are maintained for use by dba.analyze, regardless of how this is set. One of:
DBA_SCORE_READS	raw read count for interval using only reads from ChIP
DBA_SCORE_READS_FOLD	raw read count for interval from ChIP divided by read count for interval from control
DBA_SCORE_READS_MINUS	raw read count for interval from ChIP minus read count for interval from control
DBA_SCORE_RPKM	RPKM for interval using only reads from ChIP
DBA_SCORE_RPKM_FOLD	RPKM for interval from ChIP divided by RPKM for interval from control
DBA_SCORE_TMM_READS_FULL	TMM normalized (using edgeR), using ChIP read counts and Full Library size
DBA_SCORE_TMM_READS_EFFECTIVE	TMM normalized (using edgeR), using ChIP read counts and Effective Library size
DBA_SCORE_TMM_MINUS_FULL	TMM normalized (using edgeR), using ChIP read counts minus Control read counts and Full Library size
DBA_SCORE_TMM_MINUS_EFFECTIVE	TMM normalized (using edgeR), using ChIP read counts minus Control read counts and Effective Library size
DBA_SCORE_TMM_READS_FULL_CPM	same as DBA_SCORE_TMM_READS_FULL, but reporrted in counts-per-million.
DBA_SCORE_TMM_READS_EFFECTIVE_CPM	same as DBA_SCORE_TMM_READS_EFFECTIVE, but reporrted in counts-per-million.
DBA_SCORE_TMM_MINUS_FULL_CPM	same as DBA_SCORE_TMM_MINUS_FULL, but reporrted in counts-per-million.
DBA_SCORE_TMM_MINUS_EFFECTIVE_CPM	Tsame as DBA_SCORE_TMM_MINUS_EFFECTIVE, but reporrted in counts-per-million.
```

`DBA_SCORE_TMM_READS_FULL`  vs `DBA_SCORE_TMM_READS_EFFECTIVE`:

`Diffbind` let's you to choose use full library size or effective library size for trimmed mean of M values(`TMM`) normalization which was proposed by [Mark D Robinson](https://genomebiology.biomedcentral.com/articles/10.1186/gb-2010-11-3-r25)
for RNAseq. 

**Full library size** is the number of reads in the bam files.  
**Effective library size** is the number of reads mapped in the exons or within the peaks. It is the column sums for the matrix.
>Note that effective library size (bFullLibrarySize =FALSE) may be more appropriate for situations when the overall signal (binding rate) is expected to be directly comparable
between the samples.

If one wants to subtract the input reads, one can use `DBA_SCORE_TMM_MINUS_FULL` and `DBA_SCORE_TMM_MINUS_EFFECTIVE`

**No matter what score you choose, for differential binding analysis in `Diffbind`, it is always the raw counts is used for the binding matrix**.
Diffbind (by default) subtract the input raw reads for subsequent analysis. Whether or not this is good was discussed [here](https://support.bioconductor.org/p/72098/#72127).  

For example, if one uses `DESeq2`, the details are as follows:
>For each contrast, a separate analysis is performed. First, a matrix of counts is constructed for the contrast, with columns
for all the samples in the first group, followed by columns for all the samples in the second group. **The raw read count** is
used for this matrix; **if the bSubControl parameter is set to TRUE (as it is by default), the raw number of reads in the
control sample (if available) will be subtracted**. **Next the library size is computed for each sample for use in subsequent
normalization**. By default, **this is the total number of reads in peaks (the sum of each column)**. Alternatively, if the
bFullLibrarySize parameter is set to TRUE, the total number of reads in the library (calculated from the source
BAM/BED file) is used. The first step concludes with a call to DESeq2’s DESeqDataSetFromMatrix function, which
returns a DESeqDataSet object. If bFullLibrarySize is set to TRUE, then sizeFactors is called with the number of reads in the BAM/BED files for
each ChIP sample, divided by the minimum of these; otherwise, `estimateSizeFactors` is invoked.
`estimateDispersions` is then called with the `DESeqDataSet` object and `fitType` set to local. Next the model is
fitted and tested using nbinomWaldTest

`estimateSizeFactors` in DESeq2:
>Given a matrix or data frame of count data, this function estimates the size factors as follows: Each column is divided by 
the geometric means of the rows. The median (or, ir requested, another location estimator) of these ratios 
(skipping the genes with a geometric mean of zero) is used as the size factor for this column.



