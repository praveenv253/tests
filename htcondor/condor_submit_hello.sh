#!/bin/bash

# Script to generate a "submit" file and submit it to condor
# Script from Adam Hartman, modified by Matthew Beckler

#source /usr/local/condor/condor.sh

exec_name="hello"
exec_suffix=".sh"
exec_path="/afs/ece.cmu.edu/usr/praveen1/Public/condor/test-io/${exec_name}${exec_suffix}"
logdir="logs"

# Set up results directory
dir="/tmp/praveen1/${exec_name}_$(date '+%Y%m%d_%H%M%S')"
echo "Setting up results directory: $dir"
mkdir -p $dir
mkdir "$dir/$logdir"

# Condor submit file
submit_file="$dir/$exec_name.condor"

# Preamble
echo "
Executable = $exec_path
Universe = vanilla
Getenv = True
Requirements = (Arch == \"INTEL\" || Arch == \"X86_64\") && OpSys == \"LINUX\"
Copy_To_Spool = False
Priority = 0
Rank = TARGET.Mips

Output = $logdir/${exec_name}_\$(cluster)_\$(process).out
Error = $logdir/${exec_name}_\$(cluster)_\$(process).err
Log = $logdir/${exec_name}_\$(cluster)_\$(process).log

InitialDir = $dir
Should_Transfer_Files = YES
When_To_Transfer_Output = ON_EXIT
Notification = ERROR
" > $submit_file

i=0
while [ $i -lt 2 ]; do
	echo "
Arguments = $i $1
Transfer_Output_Files = test-io-$i.out
Queue
" >> $submit_file
	let i=i+1
done

# Submit to condor
#condor_submit $submit_file

# Print queue and status
#condor_q
#condor_status
