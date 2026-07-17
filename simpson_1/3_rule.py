import numpy as np
from scipy.integrate import quad
from scipy.interpolate import lagrange
import matplotlib.pyplot as plt
fun=input("Enetr the function of x using python syntax:")
def y(x):
    try:
        return eval(fun)
    except (SyntaxError,NameError,TypeError):
        print("Invalid syntax!")
        exit(0)
print("Enter the limit of intergration:")
a=float(input("Enter the lower limit:"))
b=float(input("Enter the upper limit:"))
n=int(input("Enter the no of partitions:"))
if n%2!=0:
    print("Number of partitions must be multiple of 2!")
    exit(0)
h=(b-a)/n
x=np.linspace(a,b,n+1)
Y=[y(x) for x in x]
I=0
I=Y[0]+Y[-1]
I=I+4*sum(Y[1:-1:2])
I=I+2*sum(Y[2:-1:2])
I=I*(h/3)
print(f'Approximate integral is {I:.4f}')
ext_integral=quad(lambda x:y(x),a,b,)[0]
print(f'The value of exact integral is:{ext_integral:.4f}')
error=abs(ext_integral-1)
print(f'Error= {error:.4f}')
x = np.linspace(a, b, n + 1)
x1 = np.linspace(a - 1, b + 1, 1000)

plt.figure(figsize=(10,6))
plt.plot(x1, y(x1), color='black', linewidth=2, label='f(x)')
plt.scatter(x, y(x), color='blue', zorder=5)
for i in range(0, n, 2):
    X = x[i:i+3]
    Y = y(X)
    lag_poly = lagrange(X, Y)
    L = np.linspace(X[0], X[2], 100)
    lp = lag_poly(L)
    plt.fill_between(L, 0, lp, color='pink', alpha=0.4)
    plt.plot(L, lp, color='red')
for x2 in X:
        plt.plot([x2, x2], [0, lag_poly(x2)], color='green')
plt.axhline(0, color='blue')
plt.axvline(0, color='blue')
plt.grid(True)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.title("Simpson's 1/3 Rule using Lagrange Polynomial")
plt.legend()
plt.show()
            