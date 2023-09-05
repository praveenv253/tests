#!/usr/bin/env python3

from __future__ import print_function, division

import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg as la
from scipy import stats
from sklearn import linear_model
from sklearn.pipeline import Pipeline
from sklearn.model_selection import GridSearchCV
from sklearn.cross_decomposition import CCA


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
    #np.random.seed(120)

    num_total = 1000
    num_dims = 2
    max_classif_acc = 0.9
    (X, y, Q) = gen_data(num_total, num_dims, max_classif_acc)

    #np.random.seed(12)
    #np.random.shuffle(y)

    #print(Q)

    plt.figure(figsize=(6, 6))
    plt.scatter(X[0, y==0], X[1, y==0], alpha=0.4)
    plt.scatter(X[0, y==1], X[1, y==1], alpha=0.4)

    logistic = linear_model.LogisticRegression(fit_intercept=False)
    Cs = np.logspace(-4, 4, 25)
    num_train = 700

    cca = CCA(n_components=1)
    cca.fit(X[:, :num_train].T, y)
    print(X.shape)
    print(y.shape)

    xo, yo = cca.transform(X[:, :num_train].T, y)

    pipe = Pipeline(steps=[
        ('cca', cca),
        ('logistic', logistic),
    ])
    estimator = GridSearchCV(pipe, dict(logistic__C=Cs), cv=5, n_jobs=1)
    estimator.fit(X[:, :num_train].T, y[:num_train])
    best_logistic = estimator.best_estimator_.named_steps['logistic']

    y_hat_test = best_logistic.predict(X[:, num_train:].T)
    acc = np.sum(y_hat_test == y[num_train:]) / (num_total - num_train) * 100
    print('Classification accuracy: %.3g%%' % acc)

    coef = np.squeeze(best_logistic.coef_)
    print('Coeffs of estimated separator: ', end='')
    print(coef)

    x1 = np.linspace(-6, 6, 2)
    x2 = - coef[0] * x1 / coef[1]
    plt.plot(x1, x2, 'k', linewidth=0.75)

    plt.axis('equal')
    plt.xlim((-5, 5))
    plt.ylim((-5, 5))
    plt.show()
