## Using HTCondor <span style="font-size:2;" class="muted">(in CMU)</span>

1. First, you need to design your program to be able to accept arguments that
   allow it to do a part of the whole task (that's how I'm parallelizing most
   stuff, anyway). eg. `hello.sh`

2. Then, you need to write a prep script that defines how many jobs are there
   overall, and which job does what - i.e. what arguments are to be passed to
   the program for each job. You also need to set some path parameters.
   eg. `condor_prep_hello.sh`

3. Make sure you read and understand all the comments in the prep script as
   well as in `condor_submit.sh`. The permissions issues discussed there are
   important.

4. Finally, source the prep script you wrote, followed by `condor_submit.sh`.
   This should take care of submitting all your jobs to Condor.
