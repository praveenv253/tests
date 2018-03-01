#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


# XXX This is not really an AR process, because a real AR process would have
#     an IIR filter, not an FIR filter! This is actually an MA process!

def create_ar_data(coeffs, num_pts):
    e = np.random.normal(size=(num_pts + len(coeffs) - 1))
    return np.convolve(e, coeffs, 'valid')


if __name__ == '__main__':
    n = 60
    a = create_ar_data(np.array([1, 0.9, 0.8, 0.7, 0.6]), n)
    lw = 8

    plt.figure()
    plt.plot(np.arange(n), np.zeros(n), 'k-', linewidth=lw)
    plt.plot(10 * np.ones(100), np.linspace(min(a), max(a), 100), 'k-', linewidth=lw)
    plt.plot(a, 'g-', linewidth=lw)
    plt.axis('off')

    plt.figure()
    b = a + np.random.normal(size=a.shape, scale=1.3)
    plt.plot(np.arange(n), np.zeros(n), 'k-', linewidth=lw)
    plt.plot(10 * np.ones(100), np.linspace(min(b), max(b), 100), 'k-', linewidth=lw)
    plt.plot(b, 'b-', linewidth=lw)
    plt.axis('off')

    plt.show()
