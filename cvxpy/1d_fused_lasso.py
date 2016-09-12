#!/usr/bin/env python3

from __future__ import print_function, division

"""Solves the 1D fused lasso problem"""

import sys
import numpy as np
import cvxpy as cvx
import matplotlib.pyplot as plt
import scipy.sparse as sparse

if __name__ == '__main__':
    # Problem data
    n = 1000
    x = np.ones(n)
    x[:n//2] *= -1
    y = x + np.random.normal(scale=0.1, size=(n,))

    # Set up the difference matrix for the fused lasso penalty
    diffmat_list = []
    for i in range(n):
        indices = np.array([i + 1, i - 1])
        indices = indices[(indices >= 0) & (indices < n)]
        for j in indices:
            diffmat_list.append(sparse.csr_matrix(([1, -1], ([0, 0], [i, j])),
                                                  shape=(1, n)))
    diffmat = sparse.vstack(diffmat_list, format='csr')
    #print(diffmat.toarray())

    # Construct the problem
    theta = cvx.Variable(n)
    lamda = 1
    objective = cvx.Minimize(0.5 * cvx.sum_entries(cvx.square(y - theta))
                             + lamda * cvx.norm(diffmat * theta, 1))
    prob = cvx.Problem(objective)

    print("Optimal value", prob.solve())
    plt.plot(np.linspace(0, 10, n, endpoint=False), y, 'bo', mfc='none',
             mec=(0.2, 0.3, 1), mew=1)
    plt.plot(np.linspace(0, 10, n, endpoint=False), theta.value,
             c=(1, 0.4, 0.0), linewidth=3)
    plt.show()
