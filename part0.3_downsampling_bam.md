### Downsampling reads to a certain number

When compare different ChIP-seq data sets or analyze a set of ChIP-seq data sets together (e.g. ChromHMM analysis), it is desirable 
to subsample the deeply sequenced ones to a certain number of reads (say 15million or 30 million).

In paper [Integrative analysis of 111 reference human epigenomes](http://www.nature.com/nature/journal/v518/n7539/full/nature14248.html):

>To avoid artificial differences in signal strength due to differences in sequencing
depth, all consolidated histone mark data sets (except the additional histone marks
the seven deeply profiled epigenomes, Fig. 2j) were uniformly subsampled to a
**maximum depth of 30 million reads** (the median read depth over all consolidated
samples). For the seven deeply profiled reference epigenomes (Fig. 2j), histone mark
data sets were subsampled to a maximum of 45 million reads (median depth). The
consolidated DNase-seq data sets were subsampled to a maximum depth of 50
million reads (median depth). **These uniformly subsampled data sets were then used
for all further processing steps (peak calling, signal coverage tracks, chromatin states)**.

After reading several posts [here](https://www.biostars.org/p/76791/) and [here](https://groups.google.com/forum/#!topic/bedtools-discuss/gf0KeAJN2Cw).
It seems `samtools` and `sambamba` are the tools to use, but they both output a proportion number of reads. 

```bash
time samtools view -s 3.6 -b my.bam -o subsample.bam
real	6m9.141s
user	5m59.842s
sys	0m8.912s

time sambamba view -f bam -t 10 --subsampling-seed=3 -s 0.6 my.bam -o subsample.bam
real	1m34.937s
user	11m55.222s
sys	0m29.872s
```
`-s 3.6` set seed of 3 and 60% of the reads by samtools.
Using multiple cpu with `sambamba` is much faster and an index file is generated on the fly.

If one wants to get say 15 million reads, one needs to do `samtools flag stat` or `samtools idxstats` to get the total number of reads,
and then calculate the proportion by:  `15 million/total = proportion`. 

`samtools idxstats` is much faster when the bam is sorted and indexed:
>Retrieve and print stats in the index file. The output is TAB delimited with each line consisting of reference sequence name, sequence length, # mapped reads and # unmapped reads.

Total number of reads: `samtools idxstats example.bam | cut -f3 | awk 'BEGIN {total=0} {total += $1} END {print total}'`

Finally, feed the proportion to `-s` flag. One might want to remove the unmapped the reads and the duplicated reads in the bam file before downsampling. One might also need to sort the subsampled bam file again and index it.
