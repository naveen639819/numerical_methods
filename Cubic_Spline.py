#Cubic Spline1

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt


x_data = np.array([0, 1, 2, 3])
y_data = np.array([1, 2, 33, 244])

cs = CubicSpline(x_data, y_data)

x_interp = np.linspace(0, 3, 50)
y_interp_scipy = cs(x_interp)

plt.figure()
plt.plot(x_data, y_data, 'o', label='Data points')
plt.plot(x_interp, y_interp_scipy, label='Cubic Spline')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()

x_value=2.5
y_value=cs(x_value)
print(f"The value at x={x_value} is y={y_value}")