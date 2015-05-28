#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

snr = 100             # Ratio of signal variance to noise variance
window_size = 64      # Must be even
n = window_size * 5   # Length of time
corr_threshold = 1e-3 # Absolute threshold of correlation value

# Generate pseudorandom sequence for this experiment
ps_seq = np.random.normal(size = (window_size/2,)) # Signal variance = 1
a = np.hstack((ps_seq,) * 2)

# Create b - an extended, noisy version of a
sqrt_snr = np.sqrt(snr)   # Ratio of standard deviations
noise = np.random.normal(scale=1.0/sqrt_snr, size=(n,))
b = noise
b[n/2 - window_size/2 : n/2 + window_size/2] += a

# Compute the normalized correlation of two successive windows of size
# window_size/2
left_half_windows = b[:-window_size/2]
right_half_windows = b[window_size/2:]
prod = left_half_windows * np.conj(right_half_windows)
# Unnormalized correlation
correlation = np.convolve(prod, np.ones(window_size/2), mode='valid')

left_half_prod = np.abs(left_half_windows) ** 2
right_half_prod = np.abs(right_half_windows) ** 2
left_half_var = np.convolve(left_half_prod, np.ones(window_size/2),
                            mode='valid')
right_half_var = np.convolve(right_half_prod, np.ones(window_size/2),
                             mode='valid')

# Normalized correlation, with a threshold on the absolute correlation value
normalized_correlation = np.zeros(correlation.shape)
i = np.where(abs(correlation) > corr_threshold)
normalized_correlation[i] = ( correlation[i]
                              / (left_half_var[i] * right_half_var[i]) )

plt.subplot(311)
plt.title('a(t)')
plt.plot(a)

plt.subplot(312)
plt.title('b(t)')
plt.plot(b)

plt.subplot(313)
plt.title('Running correlation over two successive windows of size %d'
          % (window_size/2))
plt.plot(correlation)

plt.tight_layout()
plt.show()
