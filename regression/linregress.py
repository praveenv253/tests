#!/usr/bin/env python

import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Make some random noisy data
    x = np.arange(1, 10, 0.1)
    y = y = x + np.random.normal(scale=0.707, size=x.shape)

    # Find the parameters of the linear fit
    ret = stats.linregress(x, y)

    # Display statistics
    print('Slope: %f' % ret[0])
    print('Intercept: %f' % ret[1])
    print('r-value: %f' % ret[2])
    print('p-value: %f' % ret[3])
    print('stderr: %f' % ret[4])

    # Plot everything
    plt.plot(x, y, 'bx')
    plt.plot(x, ret[0] * x + ret[1], 'r-')
    plt.legend(('Data', 'Linear fit'), loc='upper left')
    plt.show()
