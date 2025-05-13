#Gauss Chebyshev

import numpy as np

def gauss_chebyshev_integration(func, n):
    nodes = np.cos((2 * np.arange(1, n + 1) - 1) * np.pi / (2 * n))
    weights = np.pi / n * np.sqrt(1 - nodes**2)
    result = np.sum(func(nodes) * weights)
    return result

def integrand(x):
    return (1 - x**2)**(3/2) * np.cos(x)
n_one_point = 1
n_two_point = 2
n_three_point = 3
integral_one_point = gauss_chebyshev_integration(integrand, n_one_point)
integral_two_point = gauss_chebyshev_integration(integrand, n_two_point)
integral_three_point = gauss_chebyshev_integration(integrand, n_three_point)
print(f"One-point Gauss-Chebyshev Integration: {integral_one_point}")
print(f"Two-point Gauss-Chebyshev Integration: {integral_two_point}")
print(f"Three-point Gauss-Chebyshev Integration: {integral_three_point}")