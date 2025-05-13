#Gauss Legendre

import numpy as np

def gauss_legendre_integration(func, n, a, b):
    nodes, weights = np.polynomial.legendre.leggauss(n)
    mapped_nodes = 0.5 * (b - a) * nodes + 0.5 * (a + b)
    mapped_weights = 0.5 * (b - a) * weights

    result = np.sum(func(mapped_nodes) * mapped_weights)
    return result

def integrand(x):
    return 1/(3+4*x)

a = 0
b = 2

for n in [1, 2, 3]:
    integral_result = gauss_legendre_integration(integrand, n, a, b)
    print(f"{n}-point Gauss-Legendre Integration: {integral_result}")

