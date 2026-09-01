import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return x**2 + 2*x + 1
x = np.linspace(-5, 5, 100)
y = f(x)
print("Function: y = x^2 + 2x + 1")
print("f(2) =", f(2))
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Graph of User Defined Function")
plt.grid(True)
plt.show()