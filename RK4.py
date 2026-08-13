import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
def f(x,y):
    return x*x+y*y
x=0
y=1
t=[]
xvals=[x]
yvals=[y]
h=0.1
n=8
for i in range(n):
    k1=h*f(x,y)
    k2=h*f(x+h/2,y+k1/2)
    k3=h*f(x+h/2,y+k2/2)
    k4=h*f(x+h,y+k3)
    y=y+(k1+2*k2+2*k3+k4)/6
    x=x+h
t.append([x,y])
xvals.append(x)
yvals.append(y)
print("Result :")
t=pd.DataFrame(t,columns=['x','y']).to_string(index=False)
print(f'The required solution in {n} steps is : {t}')
lag_poly=lagrange(xvals,yvals)
plt.figure(figsize=(8,5))
plt.plot(xvals,yvals,label="RK4 solution ",marker="x")
plt.axhline(0)
plt.axvline(0)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Solution of ODE using RK4 method")
plt.grid(True)
plt.legend()
plt.show()


