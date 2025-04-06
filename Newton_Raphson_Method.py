import numpy as np

def f(x, y):
    return x**2 * y + y**3 - 10

def g(x, y):
    return x * y**2 - x**2 - 3

def newton_raphson(x, y):
    n = 0
    max_iterations = 10
    tolerance = 1e-10

    while n < max_iterations:
        # Jacobian matrix
        J = np.array([
            [2 * x * y, x**2 + 3 * y**2],
            [y**2 - 2 * x, 2 * x * y]
        ])

        # Function vector
        F = np.array([f(x, y), g(x, y)])

        try:
            delta = np.linalg.solve(J, F)  # More stable than computing the inverse
        except np.linalg.LinAlgError:
            print("Jacobian is singular or nearly singular at this step.")
            return

        x_new = x - delta[0]
        y_new = y - delta[1]

        print(f"Iteration {n + 1}: x = {round(x_new, 10)}, y = {round(y_new, 10)}")

        # Convergence check
        if np.linalg.norm([x_new - x, y_new - y], ord=2) < tolerance:
            x, y = x_new, y_new
            break

        x, y = x_new, y_new
        n += 1

    print(f"Final Root: x = {round(x, 10)}, y = {round(y, 10)}")
    print(f"Method converges after {n + 1} iterations" if n < max_iterations else "Method did not converge within the maximum number of iterations.")

# Run the method
newton_raphson(0.8, 2.2)