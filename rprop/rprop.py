#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt


def objective(vec, gamma=1e-3):
    x, y = vec[0], vec[1]
    return np.abs(x - y) - gamma * (x + y)
    #return np.abs(x - y)**2 - gamma * (x + y)


def gradient(vec, gamma=1e-3):
    x, y = vec[0], vec[1]
    return np.array([np.sign(x - y) - gamma, - np.sign(x - y) - gamma])
    #return np.array([2 * (x - y) - gamma, - 2 * (x - y) - gamma])


def project(vec):
    vec_new = np.minimum(vec, 1)
    vec_new = np.maximum(vec_new, 0)
    return vec_new


if __name__ == '__main__':
    gamma = 1
    vec = np.array([0.25, 0])

    eta = 1e-3 * np.ones(2)
    beta = 0.9       # Factor to increase or decrease LR for Rprop
    alpha = 0.999    # Slow decay of overall learning rate

    stop_threshold = 1e-6  # Absolute difference in objective for stopping
    max_iterations = 10000
    patience = 20    # Num iters with small gradient before stopping (min=1)
    extra_iters = 0  # Num of extra iters after stop criterion is attained

    minima = None
    g_prev = None
    running_obj = []
    running_vec_pre_proj = [vec.copy(),]
    running_vec_post_proj = [vec.copy(),]
    running_grad = []
    running_eta = []

    i = 1
    extra = 0
    while True:
        # Evaluate the objective
        obj = objective(vec, gamma)

        if minima is None or obj < min(running_obj):
            minima = (vec.copy(), obj)

        if len(running_obj) >= patience:
            if extra == 0:
                if (np.abs(np.array(running_obj[-patience:]) - obj) < stop_threshold).all() or i >= max_iterations:
                    if i >= max_iterations:
                        warnings.warn('Exceeded maximum number of iterations. May not have converged.')
                    if extra_iters == 0: break
                    extra += 1
            elif extra > extra_iters:
                break
            else:
                extra += 1

        if np.isnan(obj):
            running_obj.append(np.inf)
        else:
            running_obj.append(obj)
        i += 1

        g = gradient(vec, gamma)
        g = np.sign(g).astype(int)

        # Backtracking with Rprop would have to work by ensuring that
        # gradients are moving in the right direction along all dimensions.
        #
        # This won't work well in conjunction with *projected* gradient
        # descent, because the projection step may be parallel and opposite
        # to the gradient step in one dimension. If so, that dimension can
        # never be made to move in the right direction, meaning
        # backtracking will fail before convergence.

        # Vanilla gradient descent
        vec_plus = vec - alpha**i * eta * g

        # Project sig back onto the PSD cone
        vec_proj = project(vec_plus)

        # Learning rate update
        if g_prev is not None:
            sign_changed = - g * g_prev  # -1 if sign did not change, +1 if sign changed
            eta *= beta**sign_changed

        g_prev = g

        running_eta.append(eta)
        running_grad.append(g)
        running_vec_pre_proj.append(vec_plus)
        running_vec_post_proj.append(vec_proj)
        vec[:] = vec_proj

    running_vec_pre_proj = np.array(running_vec_pre_proj).squeeze()
    running_vec_post_proj = np.array(running_vec_post_proj).squeeze()
    running_grad = np.array(running_grad).squeeze()

    plt.figure()
    plt.plot(running_obj)
    plt.title('Objective')

    plt.figure()
    #plt.plot(running_vec_post_proj)
    x, y = np.mgrid[0:1:100j, 0:1:100j]
    vecs = np.array([x, y]).reshape((2, -1))
    objs = objective(vecs, gamma).reshape((100, 100))
    plt.pcolormesh(x, y, objs[1:, 1:], cmap='jet')
    plt.colorbar()
    plt.plot(running_vec_post_proj[:, 0], running_vec_post_proj[:, 1], 'w-')
    plt.plot(running_vec_post_proj[0, 0], running_vec_post_proj[0, 1], 'ko')

    plt.show()
