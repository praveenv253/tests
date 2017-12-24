#!/usr/bin/env python

'''
Description of files goes here.
'''

# System imports
import os
import sys
import time
import cPickle

# Scientific computing
import numpy as np
import scipy as sp
import scipy.linalg as lin
import scipy.ndimage as ndim
import _dxmulc

if __name__ == '__main__':
    D = np.random.rand(4, 8)
    sup = np.array([[1], [2], [5]], dtype=np.int32)
    vals = np.array([[1.3], [0.5], [-0.6]])

    y1 = _dxmulc.dxmulc(D, sup, vals)

    y2 = D[:, np.ravel(sup)].dot(vals)
