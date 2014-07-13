#!/usr/bin/env python

import numpy as np
import scipy as sp
import matplotlib.pyplot as plt


sampling_rate = 1e4 # Samples/sec
pulse_width = 1 # sec
carrier_freq = 1e2 # Hz
pi = sp.pi
sigma_noise = 0.3 # Std dev of noise

def constellation_mapper(m, scheme):
    """
    Maps bits according a modulation scheme. Returns corresponding symbols.

    Available schemes:
    - bpsk
    """
    if scheme == 'bpsk':
        # Binary phase shift keying
        # 0 -> -1
        # 1 -> 1
        s = sp.zeros(m.shape, dtype=complex)
        s[ sp.where(m == 0) ] = -1
        s[ sp.where(m == 1) ] = 1
        return s
    else:
        raise ValueError('No such scheme or scheme not available')

def construct_signal(s, p):
    """Constructs s(t) from symbols {s} and pulse shape p(t)."""
    x = sp.zeros((s.size, p.size), dtype=complex)
    x = sp.multiply(s.reshape((s.size, 1)), p)
    x = x.ravel()
    return x

def upconvert(x, fc):
    """
    Upconverts in-phase and quadrature components of a time-domain signal
    appropriately. Returns the in-phase and quadrature signals
    """
    t = sp.arange(x.size)
    x_i = sp.real(x) * 2 * sp.cos(2*pi*fc*t / sampling_rate)
    x_q = sp.imag(x) * 2 * sp.sin(2*pi*fc*t / sampling_rate)
    return x_i, x_q


if __name__ == '__main__':
    # Generate a sequence of bits.
    m = sp.array([1, 0, 1, 0])
    # Convert bits to symbols
    s = constellation_mapper(m, 'bpsk')

    # Pulse shape
    p = sp.ones(pulse_width * sampling_rate)
    # Convert symbols into signal
    x = construct_signal(s, p)

    # Upconvert the signal into passband
    x_i, x_q = upconvert(x, carrier_freq)
    # Add the signals to get the final transmit signal
    x_tx = x_i + x_q

    # Add noise to the transmit signal => channel
    n = sp.random.normal(scale=sigma_noise, size=(x_tx.size,))
    y_rx = x_tx + n

    # Get the in-phase and quadrature components out
    y = downconvert(y_rx, carrier_freq)


    #plt.stem(sp.arange(x_q.size), x_q)
    #plt.show()
