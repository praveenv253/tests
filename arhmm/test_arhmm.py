#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt


def ar(n, coeffs, sigma, start=None, mu=0):
    """
    Generates an AR process with given parameters.
        x[k] = \sum_{i=1}^p coeffs[i] * x[k - i] + \epsilon[i]
    \epsilon[i] are iid with variance `sigma`**2

    Parameters
    ----------
    n : integer
        Number of time points
    coeffs : array-like
        Autoregressive coefficients in reverse time-order (used as shown above)
    sigma : float
        Standard deviation of the Gaussian innovation term epsilon
    start :  array-like (optional; default zero)
        Optional vector of size equal to the number of coefficients
        (by default they are all taken to be zero).
    mu : float (optional; default zero)
        Optional offset for epsilon (i.e. the mean). By default it is 0.

    Returns
    -------
    x : np.ndarray of shape (n,)
        An autoregressive process generated from the given parameters
    """

    coeffs = np.array(coeffs)
    p = coeffs.size

    if start is None:
        start = np.zeros(p)
    else:
        start = np.array(start)
        if start.size != p:
            raise ValueError('start must have the same length as coeffs')

    eps = mu + sigma * np.random.randn(n)
    x = np.zeros(n + p)
    x[:p] = start
    for i in range(p, n+p):
        x[i] = np.sum(x[i-p:i][::-1] * coeffs) + eps[i-p]

    return x[p:]


if __name__ == '__main__':
    n = 1000

    s = 2      # Number of HMM states
    q = 0.005  # Symmetric switching probability
    # If state switch == 1, that means that the state switched at that instant
    state_switches = (np.random.rand(n) <= q).astype(int)
    switch_times = np.r_[0, np.where(state_switches == 1)[0], n]
    intervals = switch_times[1:] - switch_times[:-1]
    print('Number of intervals: %d' % intervals.size)

    state_coeffs = [[0.5, 0.1, 0, -0.1, -0.3], [0.9, -0.9]]
    state_sigmas = [0.5, 0.2]

    xs = []
    for i, interval in enumerate(intervals):
        c = len(state_coeffs[i % s])
        if i == 0:
            start = None
        else:
            start = xs[i-1][-c:]
            start = np.pad(start, (c - start.size, 0), 'constant',
                           constant_values=0)
        xs.append(ar(interval, state_coeffs[i % s], state_sigmas[i % s],
                     start))

    plt.figure()
    plt.plot(np.concatenate(xs))
    plt.show()

    plt.figure()
    plt.plot(np.concatenate(xs))
    for i in switch_times:
        plt.axvline(i, linestyle='--', color='C2')
    plt.show()
