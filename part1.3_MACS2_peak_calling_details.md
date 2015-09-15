
From the paper:  

>Peak calling. For the histone ChIP-seq data, the MACSv2.0.10 peak caller was used to compare ChIP-seq signal to a corresponding whole-cell extract (WCE) sequenced control to identify narrow regions of enrichment (peaks) that pass a Poisson P value threshold 0.01, broad domains that pass a broad-peak Poisson P value of 0.1 and gapped peaks which are broad domains (P < 0.1) that include at least one narrow peak (P < 0.01) (https://github.com/taoliu/MACS/)32. Fragment lengths for each data set were pre-estimated using strand cross-correlation analysis and the SPP peak caller package (https://code.google.com/p/phantompeakqualtools/)37 and these fragment length estimates were explicitly used as parameters in the MACS2 program (–shift-size = fragment_length/2).
>

The description actually is wrong in the paper. for MACS2, the 