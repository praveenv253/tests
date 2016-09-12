#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import cvxpy as cvx
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Problem data
    m = 30
    n = 20
    A = np.random.randn(m, n)
    b = np.random.randn(m)

    # Construct the problem
    x = cvx.Variable(n)
    objective = cvx.Minimize(cvx.sum_entries(cvx.square(A*x - b)))
    constraints = [0 <= x, x <= 1]
    prob = cvx.Problem(objective, constraints)

    print("Optimal value", prob.solve())
    print("Optimal var")
    print(x.value)
