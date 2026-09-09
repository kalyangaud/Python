import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 3, 1, 0])
spline = CubicSpline(x, y, bc_type='natural')

xx = np.linspace(0, 4, 100)
yy = spline(xx)
plt.plot(x, y, 'o', label='Data points')
plt.plot(xx, yy, label='Cubic Spline')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic Spline Curve")
plt.grid()
plt.legend()
plt.show()