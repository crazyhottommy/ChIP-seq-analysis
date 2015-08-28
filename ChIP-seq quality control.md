### Quality control of the ChIP-seq data.

First read the two papers in the repo README.

[ChIP-seq guidelines and practices of the ENCODE and modENCODE consortia](http://www.ncbi.nlm.nih.gov/pubmed/22955991)  
[Practical Guidelines for the Comprehensive Analysis of ChIP-seq Data](http://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1003326) 

According to a [guideline](http://cistrome.org/chilin/_downloads/instructions.pdf) from Sherily Liu's lab, I summarize the matrics below:  

1. Fastq reads median quality score >= 25. This can be get by [FASTQC from Babaraham Institute](http://www.bioinformatics.babraham.ac.uk/projects/fastqc/).
  Many other good tools like Bismark for DNA methylation data mapping, and SeqMonk, a pretty cool GUI tool alternative to IGV.  
  
  According to Kadir, the sequencing core members will do initial quality control with the fastq files and will flag the file if quality of 
  the file is bad.  In addition, they will trim off the adaptors when de-duplex.
  
2. Raw reads number. According to Encode best practise, for most transcription factors (TFs), ~10 million of reads are good enough; for 
  histone modifications, ~20 millions reads are recommended. The more reads one sequences, the more peaks will show up. However,
  the peak number will saturate when a certain number of reads (~say 30 million for TFs) are sequenced.
  
3. Uniquely mapped reads. A good uniquely mapped ratio is ≥ 60%.

4. Replicates total peaks are the total peaks number called by MACS2 with fixed extension size and qvalue cutoff. A good peaks number depends on your experiment.

5.
