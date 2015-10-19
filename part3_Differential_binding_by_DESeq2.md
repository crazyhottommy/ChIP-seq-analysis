### Differential binding by DESeq2  

There are many tools detecting differential binding for ChIP-seq data.  See [here](https://github.com/crazyhottommy/ChIP-seq-analysis#differential-peak-detection).  
 
DiffBind is very popular and internally it uses EdgR or DESeq1/2. Given that I have gotten raw counts from part2, I will use DESeq2 for differential peak detecting.  

In this way, I have a more flexiable control over the counts table. From here on, the workflow is pretty much like a RNA-seq differential gene expression workflow.

Let's normalize the raw counts by the sequencing depth (library size) first, and then **subtract the input control tags for the IP samples** (**This is wrong or not recommended!** see below) and then use the DESeq2 `estimatesizefactor` function to do the normalization.   

See my post on [bioconductor support site](https://support.bioconductor.org/p/72098/#72173)  

From DiffBind author Rory stark:
>I'm not sure what you mean by wanting to "take it the other way"? Meaning, why not use the DiffBind package, which does exactly this type of analysis? Is the idea is that you want to really control each step yourself? 

>If you want to subtract the control reads from the ChIP reads, you should do a simple scaling first. Rounding the nearest integer avoids the DESeq2 issue (you also have to check for negative values as it may be possible there there re more reads in the control than in the ChIP for some merged consensus peaks for some samples). DiffBind does this by default. In your case, it would multiply the control read counts by the ratio of ChIP:Control reads (computed individually for each sample) -- 0.50 in all of your examples -- and round the result before subtracting.

>In an experiment  like you describe, where the same tissue type is used for all the samples, subtracting the control reads shouldn't make much difference to the results as the same control is used for all the samples in each group, unless there are significant difference between the Inputs for each sample group. This should only happen if the treatment had a big impact the open chromatin (or be the result of a technical issue in the ChIP). The Input controls are most important for the MACS peak calling step.

From Ryan C.Thompson:
>You might want to take at look at the csaw package, which adapts the edgeR method with all the necessary modifications for unbiased ChIP-Seq differential binding analysis. **Also, I would not recommend subtracting input from ChIP counts, since all the count-based methods assume that you are analyzing absolute counts, not "counts in excess of background**".
>

From DESeq2 author Michael Love:
>**You should definitely never subtract or divide the counts you provide to DESeq2**.I would not use the input counts at all for differential binding. I would just compare treated counts vs untreated ChIP counts. but I would also recommend to also take a look at DiffBind and csaw vignettes and workflows, at the least to understand the best practices they've set out.

From DiffBind author Rory stark again:
>While it is certainly the case that altering the read counts using control reads violates an essential assumption underlying DESeq2 (namely the use of unadulterated read counts), ignoring the control tracks can also lead to incorrect results. This is because the binding matrix may include read counts for enriched regions (peaks) in samples where they were not originally identified as enriched compared to the control. As DESeq2 will have no way of detecting an anomaly in the Input control for that sample in that region, the results may be misleading. This is most likely to occur in experiments involving different cell types.

>There are alternative ways to incorporate the Input controls. For example, instead of scaling the control read counts, **the control libraries can be down-sampled to the same level as each corresponding ChIP sample prior to peak calling (MACS2 does this) and counting.**  This is what we do in our processing pipelines. This still involves altering the ChIP read counts via subtraction however, and in practice down-sampling and scaling almost always yield the same results.

>The other method is the more aggressive use of blacklists. **Generating blacklists based on every Input control**, and removing reads/peaks from every sample that overlap any blacklisted area, can eliminate false positives in those regions where there is an anomaly in an Input control.  Gordon Brown developed the [GreyListChIP](http://www.bioconductor.org/packages/release/bioc/html/GreyListChIP.html) package for this purpose.
>

From EdgeR author Aaron Lun:
>From what I can see, there's two choices; either we get erroneous DB calls because of differences in chromatin state and input coverage, or we get errors due to distorted modelling of the mean-variance relationship after input subtraction. Our (i.e., the edgeR development team's) opinion is that the latter is more dangerous for routine analyses of ChIP-seq count data. Inaccurate variance modelling will affect the inferences for every genomic region via EB shrinkage, while spurious calls due to differences in chromatin state should be limited to a smaller number of regions. Rory's blacklist idea might be useful here, as we would be able to screen out such problematic regions before they cause any headaches during interpretation.

In a word, subracting input control counts from the IP counts violates the DESeq2 and EdgeR assumption and should not be used. The blacklist method may be the way to go.

There is a nice tutorial using bioconductor in f1000 research [From reads to regions: a Bioconductor workflow to detect differential binding in ChIP-seq data](http://f1000research.com/articles/4-1080/v1)

