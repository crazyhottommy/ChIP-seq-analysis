### How to set MACS2 peak calling parameters


From the paper [Integrative analysis of 111 reference human epigenomes](http://www.nature.com/nature/journal/v518/n7539/full/nature14248.html):  

>Peak calling. For the histone ChIP-seq data, the MACSv2.0.10 peak caller was used to compare ChIP-seq signal to a corresponding whole-cell extract (WCE) sequenced control to identify narrow regions of enrichment (peaks) that pass a Poisson P value threshold 0.01, broad domains that pass a broad-peak Poisson P value of 0.1 and gapped peaks which are broad domains (P < 0.1) that include at least one narrow peak (P < 0.01) (https://github.com/taoliu/MACS/). Fragment lengths for each data set were pre-estimated using strand cross-correlation analysis and the [SPP peak caller package](https://code.google.com/p/phantompeakqualtools/) and these fragment length estimates were explicitly used as parameters in the MACS2 program (–shift-size = fragment_length/2).
>

MACS2 is used to call broad and narrow peaks for **histone ChIP-seq:**  
>MACSv2.0.10 was also used to call narrow peaks using the same settings specified above for the histone mark narrow peak calling.

>Narrow peaks and broad domains were also generated for the unconsolidated, 36-bp mappability filtered histone mark ChIP-seq and DNase-seq Release 9 data sets using MACSv2.0.10 with the same settings as specified above.


**The description actually is not accurate in the paper**. for MACS2
>--extsize EXTSIZE The arbitrary extension size in bp. When nomodel is true, MACS will use this value as fragment size to extend each read towards 3' end, then pile them up. **It's exactly twice the number of obsolete SHIFTSIZE.** In previous language, each read is moved 5'->3' direction to middle of fragment by 1/2 d, then extended to both direction with 1/2 d. This is equivalent to say each read is extended towards 5'->3' into a d size fragment. DEFAULT: 200. EXTSIZE and SHIFT can be combined when necessary. Check SHIFT option.
>

In the ENCODE [ChIP-seq github page](https://github.com/crazyhottommy/chip-seq-pipeline/blob/master/dnanexus/macs2/src/macs2.py) I found:

```python

   #===========================================
	# Generate narrow peaks and preliminary signal tracks
	#============================================

	command = 'macs2 callpeak ' + \
			  '-t %s -c %s ' %(experiment.name, control.name) + \
			  '-f BED -n %s/%s ' %(peaks_dirname, prefix) + \
			  '-g %s -p 1e-2 --nomodel --shift 0 --extsize %s --keep-dup all -B --SPMR' %(genomesize, fraglen)
```

```python
	#===========================================
	# Generate Broad and Gapped Peaks
	#============================================

	command = 'macs2 callpeak ' + \
			  '-t %s -c %s ' %(experiment.name, control.name) + \
			  '-f BED -n %s/%s ' %(peaks_dirname, prefix) + \
			  '-g %s -p 1e-2 --broad --nomodel --shift 0 --extsize %s --keep-dup all' %(genomesize, fraglen)


```

The fraglen is from [strand cross-correlation analysis](https://github.com/crazyhottommy/ChIP-seq-analysis/blob/master/part0_quality_control.md#calculate-fragment-length-nsc-and-rsc-by-phantompeakqualtools)


```python

#Extract the fragment length estimate from column 3 of the cross-correlation scores file
	with open(xcor_scores_input.name,'r') as fh:
		firstline = fh.readline()
		fraglen = firstline.split()[2] #third column
		print "Fraglen %s" %(fraglen)
```

### Conclusions

We are using `deeptools` for bigwig production, so we do not specify `-B`(output bedgraph) and `-SPMR`(for normalized bedgraph).

For each histone-modification ChIP-seq, we will have two sets of peaks (broad and narrow).

Use`--nomodel` and provide the `--extsize` of either 147 bp or the fragment length predicted by [strand cross-correlation analysis](https://github.com/crazyhottommy/ChIP-seq-analysis/blob/master/part0_quality_control.md#calculate-fragment-length-nsc-and-rsc-by-phantompeakqualtools) 

for narrow peaks:  
`macs2 callpeak -t IP.bam -c Input.bam -n test -p 0.01 --nomodel --extsize fragment_length --keep-dup all -g hs`  
 
for borad regions:  
`macs2 callpeak -t IP.bam -c Input.bam -n test --broad -p 0.01 --nomodel --extsize fragment_length --keep-dup all -g hs`

It turns out that ENCODE intentionally use a relax `p value 0.01` for calling peaks and then filter the peaks afterwards by [IDR](https://sites.google.com/site/anshulkundaje/projects/idr).
In my experience, I would set `q value of 0.01`([q value is to control false discover rate](http://crazyhottommy.blogspot.com/2015/03/understanding-p-value-multiple.html) )  for narrow peaks and `q value of 0.05` for broad peaks.

Please check this [issue](https://github.com/taoliu/MACS/issues/76) for MACS2:

Jgarthur:
>I ran MACS2 (2.1.0.20140616) to call peaks on chromatin accessibility data (ATAC-seq) with the following options:

`-t reads.bam -f BAM -g mm --nomodel --shift -100 --extsize 200 -p 1e-4 --broad`

>I wanted to check sensitivity to the p-value cutoff specified by -p (which I believe controls narrow peak calling before merging to broad peaks?). Running with, e.g., -p 1e-3 or -p 1e-10 gave identical output to the first run. The output is different than using -q 0.01, however. Is this the intended behavior?


Tao Liu:
>Broad peak cutoff is controlled by '--broad-cutoff'. The '-p' option controls the narrower regions inside broad regions. BTW, in the newest release, there is a new tool to give you p-value cutoff analysis "macs2 callpeak --cutoff-analysis" (without using --broad mode). It will try pvalue cutoff from 1 to 1e-10 and collect how many peaks and bps can be called as enriched regions. You may want to give it a try.

Jgarthur:
>Am I correct in saying that in --broad mode, the value set by -q or -p does not matter at all, but whether one sets -q or -p determines the meaning of --broad-cutoff as a q-value or p-value threshold?

>My own testing indicates, e.g., that "--broad -q {x} --broad-cutoff .01" is unaffected by the choice of x, though the output still displays "# qvalue cutoff = {x}"

Tao liu:
>Yes. You are right. But -q or -p also determines the narrower calls inside broad regions. MACS2 broad mode does a 2-level peak calling and embed stronger/narrower calls in weaker/broader calls.

>Thanks for reminding me this output issue. I will fix that so it will be displayed as '#qvalue cutoff for narrow region = {x}' and '# qvalue cutoff for broad region = {y}' will be correctly displayed.

