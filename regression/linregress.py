#!/usr/bin/env python

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Make some random noisy data
    rng = np.random.default_rng()
    #x = np.arange(1, 10, 0.1)  # Deterministic x
    m = 2  # True slope
    c = 1  # True intercept
    x = 10 * rng.uniform(size=100)  # Random x
    n = rng.normal(scale=np.sqrt(2), size=x.shape)
    y = m * x + c + n

    # Find the parameters of the linear fit
    ret = stats.linregress(x, y)
    slope, intercept, rval, pval, stderr = ret

    # Display statistics
    print('Slope: %f' % slope)
    print('Intercept: %f' % intercept)
    print('r-value: %f' % rval)
    print('p-value: %f' % paval)
    print('stderr: %f' % stderr)

    # Plot everything
    plt.plot(x, y, 'bx')
    plt.plot(x, ret[0] * x + ret[1], 'r-')
    plt.legend(('Data', 'Linear fit'), loc='upper left')
    plt.show()
