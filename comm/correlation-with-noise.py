#!/usr/bin/env python

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

# Random sequence
size = 32
a = sp.random.normal(size = (size,))
fft_a = np.fft.fftshift( np.fft.fft(a) )

# Pseudorandom sequence
N = 8
b = sp.hstack( (a,) * N )
fft_b = np.fft.fftshift( np.fft.fft(b) )

# Add noise to b:
snr = 0.1
noise = sp.random.normal(scale=1.0/snr, size=(size * N,))
b += noise

# Find the correlation
c = sp.correlate(b, b, 'full')

plt.subplot(411)
plt.title('A(f)')
plt.plot( abs( fft_a ) )

plt.subplot(412)
plt.title('b(t)')
plt.plot(b)

plt.subplot(413)
plt.title('B(f)')
# Note how non-zero values exist only at multiples of N.
plt.stem( sp.arange(fft_b.size), abs(fft_b) )

plt.subplot(414)
plt.title('Autocorrelation of b(t)')
plt.plot(c)

plt.show()
plt.show()
