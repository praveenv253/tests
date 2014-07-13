#!/usr/bin/env python

import scipy as sp
import scipy.weave as weave

def no_weave(a):
    b = sp.dstack(a)
    return b.sum(axis=2)

def with_weave(a):
    b = sp.zeros(a[0].shape)
    code = """
    int i, j, k;
    PyArrayObject *a_elem(400, 500);
    for( i = 0; i < 100; i++ ) {
        for( j = 0; j < 4000; j++ ) {
            for( k  0; k < 5000; k++ ) {
                a_elem = PyList_GetItem(a.ptr(), i);
                B2(i, j) = a_elem[i * 400 + j];
            }
        }
    }
    """
    weave.inline(code, ['a', 'b'])
    return b

a = []

for i in xrange(100):
    a.append(sp.rand(400, 500))

no_weave(a)
with_weave(a)
