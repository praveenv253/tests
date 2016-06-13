#!/usr/bin/env python3

"""Explicitly define the points of the 42-point sphere"""

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    # Theta, phi
    theta = []
    phi = []

    # Topmost point
    theta.append(0)
    phi.append(0)   # Doesn't matter

    # First layer of icosahedron
    for i in range(5):
        theta.append(np.pi / 2 - np.arctan(0.5))
        # 72 degrees apart
        phi.append(72 * np.pi / 180 * i)

    # Second layer of icosahedron
    for i in range(5):
        theta.append(np.pi / 2 + np.arctan(0.5))
        # 72 degrees apart, and offset by 36 degrees from the x-axis
        phi.append(72 * np.pi / 180 * i + 36 * np.pi / 180)

    # Bottommost point
    theta.append(np.pi)
    phi.append(0)   # Doesn't matter

    # Bisect the topmost point and the first layer
    for i in range(5):
        theta.append((0 + np.pi / 2 - np.arctan(0.5)) / 2)
        phi.append(72 * np.pi / 180 * i)

    # Bisect the first layer
    for i in range(5):
        theta.append(np.pi / 2 - np.arctan(0.5))
        # 72 degrees apart with an offset of 36 degrees
        phi.append(72 * np.pi / 180 * i + 36 * np.pi / 180)

    # Bisect the first and the second layer
    for i in range(10):
        theta.append(np.pi / 2)
        # 36 degrees apart, and offset by 18 degrees from the x-axis
        phi.append(36 * np.pi / 180 * i + 18 * np.pi / 180)

    # Bisect the second layer
    for i in range(5):
        theta.append(np.pi / 2 + np.arctan(0.5))
        # 72 degrees apart
        phi.append(72 * np.pi / 180 * i)

    # Bisect the bottommost point and the second layer
    for i in range(5):
        theta.append((np.pi + np.pi / 2 + np.arctan(0.5)) / 2)
        phi.append(72 * np.pi / 180 * i + 36 * np.pi / 180)

    # Convert to cartesian coordinates
    theta = np.array(theta)
    phi = np.array(phi)
    x = np.sin(theta) * np.cos(phi)
    y = np.sin(theta) * np.sin(phi)
    z = np.cos(theta)

    # Save x, y and z
    a = np.arange(42)
    np.savetxt('points-42.out', np.vstack((a, a, x, y, z)).T)
