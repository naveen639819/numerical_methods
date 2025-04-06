#Gauss Jacobi

import numpy as np

def gauss_jacobi(A, b, initial_guess):
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)

    P = np.linalg.inv(D)
    H = -P @ (L+U)
    C = P @ b

    x = np.array(initial_guess, dtype=float)

    for k in range(50):
        x_new = H @ x + C
        error = np.linalg.norm(A @ x_new - b, ord=np.inf)

        print(f"Iteration {k + 1} -  Solution: {x_new},  Error= {error}")

        if error < 1e-2:
            return x_new

        x = x_new

    raise ValueError("Gauss-jacobi method did not converge.")

A = np.array([[4, 1, 1],
              [1, 5, 2],
              [1, 2, 3]], dtype=float)
b = np.array([2, -6, -4], dtype=float)
initial_guess = [0.5, -0.5, -0.5]

solution = gauss_jacobi(A, b, initial_guess)
print("\nFinal Solution:", solution)