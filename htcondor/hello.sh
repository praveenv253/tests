#!/bin/bash

# Write something to stdout
echo "Hello from `uname -n`, arg = '$1'"

# Create an output file of some sort
echo "`uname -n`, arg = '$1'" > "test-io-$1.out"
