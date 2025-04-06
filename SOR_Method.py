#SOR method

import numpy as np

def sor_method(A, b, initial_guess):
    D = np.diag(np.diag(A))
    L = np.tril(A, k=-1)
    U = np.triu(A, k=1)
    w=1.7157

    P = np.linalg.inv(D+w*L)
    H = P @ ((1-w)*D-w*U)
    C = w*P @ b

    x = np.array(initial_guess, dtype=float)

    for k in range(100):
        x_new = H @ x + C
        error = np.linalg.norm(A @ x_new - b, ord=np.inf)

        print(f"Iteration {k + 1} -  Solution: {x_new},  Error: {error}")

        if error < 0.01:
            return x_new

        x = x_new

    raise ValueError("SOR method did not converge.")

A = np.array([[2, -1, 0],
              [-1, 2, -1],
              [0, -1, 2]], dtype=float)
b = np.array([7, 1, 1], dtype=float)
initial_guess = [1, 1, 1]

solution = sor_method(A, b, initial_guess)

print("\nFinal Solution:", solution)