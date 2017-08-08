#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy import stats
from sklearn import preprocessing, svm
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV


def gen_random_orthogonal_matrix(d):
    A = np.random.randn(d, d)
    Q, R = la.qr(A)
    lamda = R.diagonal().copy()
    lamda /= np.abs(lamda)
    return np.dot(Q, np.diag(lamda))


def gen_data(n, d, c, p=0.5):
    """
    Generate a two-class dataset for classification.

    n: number of data points
    d: dimensionality of each data point
    c: max. classification accuracy (distinguishability)
    p: probability of the first class
    """

    y = np.random.rand(n)
    y = np.where(y <= p, 0, 1)

    mu = stats.norm.ppf(c)
    t = np.empty((d, n))
    t[0, :] = mu * (1 - 2*y) + np.random.randn(n)
    if d > 1:
        t[1:, :] = np.random.randn(d-1, n)

    Q = gen_random_orthogonal_matrix(d)
    X = np.dot(Q, t)

    return (X, y, Q)


if __name__ == '__main__':
    num_total = 1000
    num_dims = 2
    max_classif_acc = 0.99
    (X, y, Q) = gen_data(num_total, num_dims, max_classif_acc)

    #print(Q)

    X = preprocessing.scale(X.T).T

    plt.figure(figsize=(6, 6))
    plt.scatter(X[0, y==0], X[1, y==0], alpha=0.4)
    plt.scatter(X[0, y==1], X[1, y==1], alpha=0.4)

    # classifer = svm.LinearSVC(fit_intercept=False)
    classifer = svm.SVC(kernel='rbf')
    # Cs = np.logspace(-4, 4, 25)
    Cs = np.logspace(-2, 2, 5)
    gammas = np.logspace(-2, 2, 5)
    num_train = 700

    pipe = Pipeline(steps=[('svc', classifer)])
    estimator = GridSearchCV(pipe, dict(svc__C=Cs, svc__gamma=gammas), cv=5,
                             n_jobs=5)
    estimator.fit(X[:, :num_train].T, y[:num_train])
    best_svc = estimator.best_estimator_.named_steps['svc']

    y_hat_test = best_svc.predict(X[:, num_train:].T)
    acc = np.sum(y_hat_test == y[num_train:]) / (num_total - num_train) * 100
    print('Classification accuracy: %.3g%%' % acc)

    # coef = np.squeeze(best_svc.coef_)
    # print('Coeffs of estimated separator: ', end='')
    # print(coef)

    # x1 = np.linspace(-6, 6, 2)
    # x2 = - coef[0] * x1 / coef[1]
    # plt.plot(x1, x2, 'k', linewidth=0.75)

    x1, x2 = tuple(np.mgrid[-6:6:1000j, -6:6:1000j])
    x1x2 = np.c_[x1.ravel(), x2.ravel()]
    # x1x2 = preprocessing.scale(x1x2)
    plt.contourf(x1, x2, best_svc.predict(x1x2).reshape((1000, 1000)),
                 cmap=plt.cm.Greys, alpha=0.2)

    plt.axis('equal')
    plt.xlim((-5, 5))
    plt.ylim((-5, 5))
    plt.show()
