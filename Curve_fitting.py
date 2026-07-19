import numpy as np
import matplotlib.pyplot as plt
print("TO FIT A SECOND DEGREE CURVE y = a + bx + cx^2 TO THE GIVEN DATA")
x = list(map(float, input("Enter x values separated by space: ").split()))
y = list(map(float, input("Enter y values separated by space: ").split()))
if len(x) != len(y):
    print("Number of x-data and y-data must be equal!")
    exit()
x = np.array(x)
y = np.array(y)
n = len(x)
print("\nData points are:")
print("   x\t\t y")
for i in range(n):
    print(f"{x[i]:8.3f}\t{y[i]:8.3f}")
sx = np.sum(x)
sx2 = np.sum(x**2)
sx3 = np.sum(x**3)
sx4 = np.sum(x**4)
sy = np.sum(y)
sxy = np.sum(x * y)
sx2y = np.sum((x**2) * y)
A = np.array([
    [n, sx, sx2],
    [sx, sx2, sx3],
    [sx2, sx3, sx4]
])
B = np.array([
    sy,
    sxy,
    sx2y
])
coeff = np.linalg.solve(A, B)
a = coeff[0]
b = coeff[1]
c = coeff[2]
print("\nCoefficient Matrix A:")
print(A)
print("\nOutput Matrix B:")
print(B)
print("\nCoefficients:")
print(f"a = {a:.4f}")
print(f"b = {b:.4f}")
print(f"c = {c:.4f}")
print(f"\nSecond Degree Polynomial:")
print(f"y = {a:.6f} + ({b:.6f})x + ({c:.6f})x²")
X = np.linspace(min(x)-5, max(x)+5, 1000)
Y = a + b*X + c*X**2
plt.plot(X, Y, label="Parabola of Best Fit")
plt.scatter(x, y, color='red', label="Data Points")
plt.axhline(0, color='red')
plt.axvline(0, color='red')
plt.grid(True)
plt.title("Second Degree Curve Fitting")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()