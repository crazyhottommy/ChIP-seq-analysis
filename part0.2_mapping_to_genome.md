I usually use bowtie1 for mapping short 36-bp reads to human genome.
bowtie2 is better for longer reads.

bowtie1:
```bash
bowtie -p 10 --best --chunkmbs 200 path/to/ref/genome -q my.fastq -S | samtools view -bS - > unsorted.bam
```

>BWA-MEM is recommended for query sequences longer than ~70bp for a variety of error rates (or sequence divergence). 
> Generally, BWA-MEM is more tolerant with errors given longer query sequences as the chance of missing all seeds is small.
> As is shown above, with non-default settings, BWA-MEM works with Oxford Nanopore reads with a sequencing error rate over 20%.


Use [Teaser](https://github.com/Cibiv/Teaser) to test which mapper works the best for you.
