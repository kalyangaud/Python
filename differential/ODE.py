import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

ode = input("Enter dy/dx in terms of x and y:")

def f(x, y):
    try:
        return eval(ode)
    except (SyntaxError, NameError, TypeError):
        print("Invalid Operation!")
        exit(0)

x = float(input("Enter the initial value of x:"))
y = float(input("Enter the initial valur of y:"))
h = float(input("Enter the step size:"))
n = int(input("Enter the no of step:"))

xvals = [x]
yvals = [y]
result = []

for i in range(n):
    k1 = h * f(x, y)
    k2 = h * f(x + h/2, y + k1/2)
    k3 = h * f(x + h/2, y + k2/2)
    k4 = h * f(x + h, y + k3)

    y = y + (k1 + 2*k2 + 2*k3 + k4) / 6
    x = x + h

    result.append([x, y])
    xvals.append(x)
    yvals.append(y)

result = pd.DataFrame(result, columns=["x", "y"]).to_string(index=False)

print(f"Requires Solution in {n} steps:\n {result}")

lag_poly = lagrange(xvals, yvals)

plt.figure(figsize=(8, 5))
plt.plot(xvals, lag_poly(xvals), label="R-K-4 soltuion", marker="x")
plt.axhline(0)
plt.axvline(0)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of ODE using R-K-4 method")
plt.legend()
plt.grid(True)
plt.show()