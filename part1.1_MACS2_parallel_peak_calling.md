
I want to use MACS2 call ChIP-seq peaks for 10 samples(each with IP and input control) with 4 different set of parameters. That's a lot of commands to type.


First, put the sample names (prefix) in to a file: 
`ls -1 *bam | sort | sed -r 's/-[A-G]{1}-NC.sorted.bam//g' | sort | uniq > sample_name.txt`  

`A` is IP. `G` is input control. 
the prefix could be anything that tags each experiment.

```bash
#! /bin/bash

## put the unique sample names into an array 
sample_files=($(cut -f 1 sample_name.txt))

# print out all the element in the array
echo "${sample_files[@]}"

## loop over the samples and call peak with macs2  

for file in "${sample_files[@]}"
do
	IP_bam="${file}"-A-NC.sorted.bam
	Input_bam="${file}"-G-NC.sorted.bam
	# call regular sharp peaks
	macs2 callpeak -t "$IP_bam" -c "$Input_bam" -g hs -n "${file}"-A-NC-regular-model -q 0.01 
	macs2 callpeak -t "$IP_bam" -c "$Input_bam" -g hs -n "${file}"-A-NC-regular-nomodel -q 0.01 --nomodel --extsize 146
	
	# call broad peak 
	macs2 callpeak -t "$IP_bam" -c "$Input_bam" --broad -g hs --broad-cutoff 0.1 -n "${file}"-A-NC-broad-model 
	macs2 callpeak -t "$IP_bam" -c "$Input_bam" --broad -g hs --broad-cutoff 0.1 -n "${file}"-A-NC-broad-nomodel --nomodel --extsize 146
done
```
This is not good, because the script will loop over all the bam files and 
call peaks one after another. It does not take advantage of the multi-thread
computing cluster.  
Assume, we have 10 distinct names in the sample_name.txt and each peak calling takes 15mins. Total time will be: 4 x 10 x 15 = 600 mins = 10 hours!

**we can do things like this in the above script**:
`macs2 callpeak -t "$IP_bam" -c "$Input_bam" -g hs -n "${file}"-A-NC-regular-model -q 0.01 &` 

Adding `&` in the end will put the program in the background and start the next command, but it will inititate as many instances as cpus . This is not good citizen behavior on a shared computing cluster.


**Alternatively, we can use `xargs` `-P` flag to restrict the number of CPUs a command uses.**

```bash
### call peaks can be parallelized by xargs

### call regular sharp peaks with model
cat sample_name.txt | xargs -P 6  -I{} macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam -g hs -n {}-A-NC-sharp-model -q 0.01 --outdir {}-A-NC-sharp-model-peaks


### call regular sharp peaks without model

cat sample_name.txt | xargs -P 6  -I{} macs2 callpeak -t {}-A-NC.sorted.bam \
-c {}-G-NC.sorted.bam -g hs -n {}-A-NC-regular-nomodel -q 0.01 \
 --nomodel --extsize 146 --outdir {}-A-NC-sharp-nomodel-peaks 


### call broad peaks with model
cat sample_name.txt | xargs -P 6  -I{} macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam --broad -g hs --broad-cutoff 0.1 -n {}-A-NC-broad-model \
 --outdir -n {}-A-NC-broad-model-peaks

### call broad peaks without model
cat sample_name.txt | xargs -P 6  -I{} macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam --broad -g hs --broad-cutoff 0.1 -n {}-A-NC-broad-nomodel \
 --nomodel --extsize 146 --outdir {}-A-NC-broad-nomodel-peaks
```

However, the standard error will be put together and hard to track for each peak calling. 

Bioinformatics Data skills by Vince Buffalo page 420:
>One stumbling block beginners frequently encounter is trying to use pipes and redirects with xargs. This won't work, as the shell process that reads your xargs xommand will interpret pipesand redirects as what to do with xarg's ouput, not as part of the command run by xargs.


One can put the macs2 peak calling script in a bash script `script.sh` redrecting the stderr to a file, and then feed it into `xargs`.

```bash
#! /bin/bash

macs2 callpeak -t "$1"-A-NC.sorted.bam \
 -c "$1"-G-NC.sorted.bam --broad -g hs --broad-cutoff 0.1 -n "$1"-A-NC-broad-nomodel \
 --nomodel --extsize 146 --outdir "$1"-A-NC-broad-nomodel-peaks \
 2> "$1"-A-NC-broad-nomodel-peaks.stder

```
use `-n 1` to restrict one input argument one time.

```bash
cat sample_name.txt | xargs -P 6 -n 1 bash script.sh

```
  
Finally use `GNU Parallel` which works with pipe and redirection:  

```bash
### call peaks can be parallelized by GNU parallel

### call regular sharp peaks with model
cat sample_names.txt | parallel --max-procs=12 'macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam -g hs -n {}-A-NC-sharp-model -q 0.01 --outdir {}-A-NC-sharp-model-peaks 2> {}-A-NC-sharp-model.stderr'


### call regular sharp peaks without model

cat sample_names.txt | parallel --max-procs=12 'macs2 callpeak -t {}-A-NC.sorted.bam \
-c {}-G-NC.sorted.bam -g hs -n {}-A-NC-sharp-nomodel -q 0.01 \
 --nomodel --extsize 146 --outdir {}-A-NC-sharp-nomodel-peaks 2> {}-A-NC-sharp-nomodel.stderr'


### call broad peaks with model
cat sample_names.txt | parallel --max-procs=12 'macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam --broad -g hs --broad-cutoff 0.1 -n {}-A-NC-broad-model -q 0.01 \
 --outdir {}-A-NC-broad-model-peaks 2> {}-A-NC-broad-model.stderr'

### call broad peaks without model
cat sample_names.txt | parallel --max-procs=12 'macs2 callpeak -t {}-A-NC.sorted.bam \
 -c {}-G-NC.sorted.bam --broad -g hs --broad-cutoff 0.1 -n {}-A-NC-broad-nomodel -q 0.01 \
 --nomodel --extsize 146 --outdir {}-A-NC-broad-nomodel-peaks 2> {}-A-NC-broad-nomodel.stderr'

```
**within 30mins, I finished peak calling for 10 x 4 = 40 MACS runs**

Read the tutorial on [biostars](https://www.biostars.org/p/63816/)  
and more bioinformatics centered tutorial by [Pierre Lindenbaum](http://figshare.com/articles/GNU_parallel_for_Bioinformatics_my_notebook/822138)   
A post by Stephen Turner [find | xargs ... Like a Boss](http://www.gettinggeneticsdone.com/2012/03/find-xargs-like-boss.html) 
