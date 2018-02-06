#!/usr/bin/env python3

from __future__ import print_function, division

import functools
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def update_(circle, xline, yline, x, y, i):
    circle.set_data(x[:i], y[:i])
    xline.set_data(np.r_[:i], x[:i])
    yline.set_data(np.r_[:i], y[:i])
    return (circle, xline, yline)


if __name__ == '__main__':
    theta = np.linspace(0, 2*np.pi, 100)
    x = np.cos(theta)
    y = np.sin(theta)

    fig, (ax1, ax2) = plt.subplots(2, 1)
    (circle,) = ax1.plot([], [])
    ax1.set_xlim(-1.5, 1.5)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_aspect('equal')

    (xline,) = ax2.plot([], [])
    (yline,) = ax2.plot([], [])
    ax2.set_xlim(0, 100)
    ax2.set_ylim(-1.5, 1.5)

    update = functools.partial(update_, circle, xline, yline, x, y)

    # You need to hold a reference to this animation object -- here `ani` --
    # even if you don't use it, to prevent it from being garbage-collected
    ani = animation.FuncAnimation(fig, update, np.r_[:100], interval=25,
                                  blit=True)
    plt.show()
