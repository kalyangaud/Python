import numpy as np
import matplotlib.pyplot as plt
eqn = input("Enter dy/dx = ")
def f(x, y):
    try:
        return eval(eqn)
    except (SyntaxError, NameError, TypeError):
        print("Invalid equation!")
        exit()
x0 = float(input("Enter initial value of x: "))
y0 = float(input("Enter initial value of y: "))
h = float(input("Enter step size (h): "))
xn = float(input("Enter final value of x: "))
x_values = [x0]
y_values = [y0]
x = x0
y = y0
print("\nIteration\t x\t\t y")
print("--------------------------------")
i = 0
while x < xn:
    print(f"{i}\t\t{x:.4f}\t\t{y:.6f}")
    y = y + h * f(x, y)
    x = x + h
    x_values.append(x)
    y_values.append(y)
    i += 1
print(f"{i}\t\t{x:.4f}\t\t{y:.6f}")
plt.plot(x_values, y_values, 'bo-', label='Euler Method')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Solution of First Order Differential Equation")
plt.grid(True)
plt.legend()
plt.show()