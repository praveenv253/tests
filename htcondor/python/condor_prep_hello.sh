#!/bin/bash

## Variables and functions that this file should define
#
# Executable's details:
# - exec_path
#   Executable's name if findable by `which`, else full path to the executable
#
# Job details:
# - task_name
#   Name of this program
# - num_jobs
#   Number of jobs to create. get_args and get_outfile_name should be able to
#   handle these many job numbers (see below).
#
# Division of labour:
# - get_args()
#   A function that accepts the job number (1..$num_jobs), and defines a
#   variable called `args` - the arguments to be passed to the executable for
#   that job number.
# - get_outfile_name()
#   A function that accepts the job number (1..$num_jobs), and defines a
#   variable called `outfile_name`, containing a comma separated list of the
#   names of output files that the executable produces for that job number.
# - get_jobspec()
#   An optional function that accepts the job number (1..$num_jobs), and
#   defines a variable called `jobspec` that contains a suitable job
#   description, possibly for parsing while post-processing.

## Note about file permissions:
#
# The condor_dir and its subdirs should have suitable file permissions, so that
# they are readable by remote machines.
#
# Check UNIX file permissions with `ls -l` and edit them using `chmod`.
# - The requisite files should at least have `a+r`.
#
# Check AFS ACL settings using `fs la` and edit them using `fs sa`.
# - The directories should at least have `rl` for system:ece.
# - For instance, recursively set condor_dir to have suitable permissions, use:
#       find $condor_dir -type d -exec fs sa {} system:ece rl \;

# Condor directory - directory containing code source repository and other
# necessary repositories (eg. fieldtrip).
condor_dir="$HOME/Public/condor"

# Name of this task - used to name the results folder and the log files.
task_name="hello"

# Path to executable, or just the file itself, if the shell can find it.
# This will be called via indirection.
exec_path="$condor_dir/tests/htcondor/python/hello.py"

# Program arguments and output file names
get_args() {
	args="$1"
}
get_outfile_name() {
	outfile_name="test-hello-${1}.out"
}

# Job description
get_jobspec() {
	# Assume that get_args and get_outfile_name are called before get_jobspec.
	jobspec="$args $outfile_name"
}

# Job details
num_jobs=2
