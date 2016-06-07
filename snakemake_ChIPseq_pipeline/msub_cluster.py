
#!/usr/bin/env python3

## In order to submit all the jobs to the moab queuing system, one needs to write a wrapper.
## This wrapper is inspired by Daniel Park https://github.com/broadinstitute/viral-ngs/blob/master/pipes/Broad_LSF/cluster-submitter.py
## I asked him questions on the snakemake google group and he kindly answered: https://groups.google.com/forum/#!topic/snakemake/1QelazgzilY

import sys
import re
from snakemake.utils import read_job_properties

## snakemake will generate a jobscript containing all the (shell) commands from your Snakefile. 
## I think that's something baked into snakemake's code itself. It passes the jobscript as the last parameter.
## https://bitbucket.org/snakemake/snakemake/wiki/Documentation#markdown-header-job-properties

jobscript = sys.argv[-1]
props = read_job_properties(jobscript)





