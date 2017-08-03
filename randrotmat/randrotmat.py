#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la


def gen_random_orthogonal_matrix(d):
    A = np.random.randn(d, d)
    Q, R = la.qr(A)
    lamda = R.diagonal().copy()
    lamda /= np.abs(lamda)
    return np.dot(Q, np.diag(lamda))


if __name__ == '__main__':
    for i in range(1000):
        Q = gen_random_orthogonal_matrix(2)
        x = (1 + 0.1 * np.random.rand(1)) * np.dot(Q, np.array([1, 0]))
        plt.plot(x[0], x[1], 'C0o')
    plt.show()

