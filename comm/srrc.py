#!/usr/bin/env python

"""
Square root raised cosine in time domain.
"""

import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

N = 1024

# P(f) = | 1,                               384 <= f < 640
#        | 0.5 + 0.5 * cos(pi*(f+256)/256), 128 <= f < 384
#        | 0.5 - 0.5 * cos(pi*(f-768)/256), 640 <= f < 896
#        | 0,                               otherwise
f = sp.arange(N/4)
P = sp.zeros(N)
P[3*N/8:5*N/8] = 1
P[N/8:3*N/8] = 0.5 + 0.5 * sp.cos(sp.pi * (f + 2*N/8) / (2*N/8))
P[5*N/8:7*N/8] = 0.5 - 0.5 * sp.cos(sp.pi * (f - 6*N/8) / (2*N/8))

plt.figure(0)
plt.subplot(311)
plt.plot(sp.arange(P.size), P)
plt.title(r'$|P(f)|$')

G = sp.sqrt(P)
plt.subplot(312)
plt.plot(sp.arange(G.size), G)
plt.title(r'$G(f) = \sqrt{|P(f)|}$')

g = np.fft.fftshift( np.fft.ifft(np.fft.fftshift(G)) )
# subset_size can go from 0 to N/2
subset_size = 50
subset = slice((g.size/2 - subset_size/2), (g.size/2 + subset_size/2))
plt.subplot(313)
plt.plot(sp.arange(g[subset].size), g[subset])
plt.title(r'$g(t) = \mathcal{F}^{-1}\{G(f)\}$')

plt.tight_layout()
plt.show()

