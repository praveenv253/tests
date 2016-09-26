#!/bin/bash

echo "`uname -n`: exec = '$@'"
export PATH="$HOME/.py3-virtualenvs/py3-numpy/bin:$PATH"
export PYTHONHOME="$HOME/.local"
export WORKON_HOME="$HOME/.py3-virtualenvs"
source "$HOME/.py3-virtualenvs/py3-numpy/bin/virtualenvwrapper.sh"
workon py3-numpy
"$@"
