#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
from joblib import Parallel, delayed

if __name__ == '__main__':
    # Example from docs
    res = Parallel(n_jobs=2)(delayed(np.sqrt)(i**2) for i in range(10))
    print(res)

    # More typical use-case
    a = 25
    def kernel(i):
        return a * i
    res = Parallel(n_jobs=2)(delayed(kernel)(i) for i in range(10))
    print(res)
