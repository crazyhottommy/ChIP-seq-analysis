
see a [post](https://groups.google.com/forum/#!topic/snakemake/iDnr3PIcsfE)  

>Apart from the rule declarations, Snakefiles are plain Python. In your return statement in myfunc, you take the value of the wildcards   
object and put braces around it. Braces around an object in Python create 
a set containing that object. But you just want the value, without wrapping it in a set. Hence, the solution is to remove the braces. 

You should put `{}` around the wildcards within quotes, like so
`"{wildcards.kittens}"`

If you are using wildcards within code you do not need the curly braces, so you can just do 
for kitten in wildcards.kittens:
    print(kitten)
    
parameters useful:

```
--keep-going, -k      Go on with independent jobs if a job fails.
```
### test functions in a python console

```bash
from snakemake.io import glob_wildcards, expand
```
### python versions
`snakemake` is python3 based, if you want to execute python2 commands, you have to activate the python2x environment.
In a future release, the environment will be baked in to snakemake so you can specify environment inside a rule.
see [this issue and pull reques: Integration of conda package management into Snakemake](https://bitbucket.org/snakemake/snakemake/pull-requests/92/wip-integration-of-conda-package/diff)

```python
rule a:
    output:
        "test.out"
    environment:
        "envs/samtools.yaml"
    shell:
        "samtools --help > {output}"

```

with `envs/samtools.yaml` being e.g.

```
channels:
  - bioconda
  - r
dependencies:
  - samtools ==1.3
```

some threads that are useful:  
* [unifying resources and cluster config](https://bitbucket.org/snakemake/snakemake/issues/279/unifying-resources-and-cluster-config)
