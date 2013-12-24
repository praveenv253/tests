#!/bin/bash

./first 1>out 2>err 3>&2 2>&1 1>&3 3>&-
