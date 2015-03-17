#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Random sequence
size = 32
a = np.random.normal(size = (size,))      # Signal variance = 1

# Pseudorandom sequence
N = 8
b = np.hstack((a,) * N)
fft_b = np.fft.fftshift(np.fft.fft(b))

# Add noise to b:
snr = 0.01   # Ratio of signal variance to noise variance
sqrt_snr = np.sqrt(snr)   # Ratio of standard deviations
noise = np.random.normal(scale=1.0/sqrt_snr, size=(size * N,))
b += noise

# Compute the normalized correlation
c = np.correlate(b, b, 'full') / np.sum(b ** 2)

plt.subplot(411)
plt.title('a(t)')
plt.plot(np.hstack((a,) * N ))

plt.subplot(412)
plt.title('a(t) in blue, b(t) in green')
plt.plot(np.hstack((a,) * N ))
plt.plot(b)

plt.subplot(413)
plt.title('B(f)')
# Note how non-zero values exist only at multiples of N.
plt.stem(np.arange(fft_b.size), abs(fft_b))

plt.subplot(414)
plt.title('Autocorrelation of b(t)')
plt.plot(c)

plt.tight_layout()
plt.show()
