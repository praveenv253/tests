#!/usr/bin/env python

from distutils.core import setup, Extension
import numpy.distutils.misc_util
import numpy

setup(
    ext_modules=[Extension("_dxmulc", ["_dxmulc.c", "dxmulc.c"])],
    include_dirs=[numpy.get_include(), '.'],
)
