#Cubic Spline2

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

def cubic_spline(x, y):
    n = len(x)
    h = np.diff(x)

    A = np.zeros((n, n))
    for i in range(1, n-1):
        A[i, i-1:i+2] = [h[i-1], 2 * (h[i-1] + h[i]), h[i]]

    A[0, 0] = 1
    A[-1, -1] = 1

    B = np.zeros(n)
    B[1:-1] = 3 * ((y[2:] - y[1:-1]) / h[1:] - (y[1:-1] - y[:-2]) / h[:-1])

    c = np.linalg.solve(A, B)

    a = y[:-1]
    b = (y[1:] - y[:-1]) / h - h * (2 * c[:-1] + c[1:]) / 3
    d = (c[1:] - c[:-1]) / (3 * h)

    polynomials = [lambda xi, a=a_i, b=b_i, c=c_i, d=d_i, xi_index=i: a_i + b_i * (xi - x[i]) +
                   c_i * (xi - x[i]) ** 2 + d_i * (xi - x[i]) ** 3 for i, (a_i, b_i, c_i, d_i) in enumerate(zip(a, b, c, d))]

    return polynomials, a, b, c, d

x_data = np.array([0, 1, 2, 3])
y_data = np.array([1, 2, 33, 244])

spline_polynomials, a, b, c, d = cubic_spline(x_data, y_data)


for i, polynomial in enumerate(spline_polynomials):
    print(f"Interval {i}:")
    print(f"a_{i} = {a[i]}")
    print(f"b_{i} = {b[i]}")
    print(f"c_{i} = {c[i]}")
    print(f"d_{i} = {d[i]}")
    print()