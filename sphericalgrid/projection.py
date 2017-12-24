#!/usr/bin/env python3

"""
An implementation of the Icosahedron projection method described in Max
Tegmark's paper (http://dx.doi.org/10.1086/310310).
"""

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # A grid is made up of triangles. These triangles can be divided in many
    # ways.
    # Each triangle is made up of three edges.
    # Each edge is made up of two vertices.
