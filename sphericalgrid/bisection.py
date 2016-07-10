#!/usr/bin/env python3

"""
Constructs a spherical grid using the bisection method.
"""

#
# XXX This script has a bug - the bisection is not performed along the arcs of
#     great circles; it is performed along latitudes. This needs to be
#     corrected.
#

from __future__ import print_function, division

import sys

import numpy as np
import matplotlib.pyplot as plt


def compute_num_phis(num_levels):
    """Computes the number of phi-points for each theta value"""
    if num_levels == 0:
        return [0, 5, 5, 0]
    else:
        num_phis_prev = compute_num_phis(num_levels - 1)
        ret = []
        for x, y in zip(num_phis_prev[:-1], num_phis_prev[1:]):
            ret.extend([2 * x, x + y])
        ret.append(0)
    return ret


def compute_shifts(num_levels):
    """Computes the extent of shift in the phi-values for each theta value"""
    if num_levels == 0:
        return [0, 0, np.pi / 5, np.pi / 5]
    else:
        shifts_prev = compute_shifts(num_levels - 1)
        ret = []
        for x, y in zip(shifts_prev[:-1], shifts_prev[1:]):
            ret.extend([x, (x + y) / 2])
        ret.append(np.pi / 5)
    return ret


def construct_grid(num_levels):
    """
    Constructs a spherical grid using num_levels levels of bisection.

    If num_levels=0, then an icosahedron is returned. For each level above 0,
    one bisection is perfromed.

    Returns two lists, thetas and phis. thetas contains the theta value of each
    bisection level. phis is a list of lists, comprising of the phi values for
    each theta value in thetas.
    """
    num_phis = compute_num_phis(num_levels)
    shifts = compute_shifts(num_levels)

    num_thetas = len(num_phis)
    thetas = np.linspace(0, np.pi, num_thetas)

    phis = []
    for num_phi, shift in zip(num_phis, shifts):
        if num_phi == 0:
            phi_theta = np.array([0., ])
        else:
            phi_theta = np.linspace(0, 2 * np.pi, num_phi, endpoint=False)
        phi_theta += shift
        phis.append(phi_theta)

    return thetas, phis


if __name__ == '__main__':
    if len(sys.argv) != 2 or sys.argv[1] in ['-h', '--help']:
        sys.exit('Usage: %s <num_levels>' % sys.argv[0])

    num_levels = int(sys.argv[1])

    thetas, phis = construct_grid(num_levels)
    all_thetas = []
    all_phis = []
    for i, theta in enumerate(thetas):
        for phi in phis[i]:
            all_thetas.append(theta)
            all_phis.append(phi)

    all_thetas = np.array(all_thetas)
    all_phis = np.array(all_phis)

    x = np.sin(all_thetas) * np.cos(all_phis)
    y = np.sin(all_thetas) * np.sin(all_phis)
    z = np.cos(all_thetas)

    a = np.arange(len(all_thetas))
    np.savetxt('points-%d.out' % a.size, np.vstack((a, a, x, y, z)).T)
