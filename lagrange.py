import numpy as np 
import sympy as sp
import matplotlib.pyplot as plt
n=int(input("Enter the number of elements:"))
X=list(map(float,input("Enter all the values of x using space:").split()))
Y=list(map(float,input("Enter all the values of y using space:").split()))
if len(X)!=len(Y):
    print("Mismatched Data!")
    exit(0)
print("Data Points are:")
print(f"X: {X}")
print(f"Y: {Y}")
x=sp.symbols("x")
lp=0
for i in range(n):
    bp=1
    for j in range(n):
        if j!=i:
            bp=bp*(x-X[j])/(X[i]-X[j])
    lp=lp+Y[i]*bp
lag_poly=sp.nsimplify(lp.evalf(),rational=True,tolerance=1e-10)
lag_poly1=sp.simplify(lag_poly)
print(f"Lagrange polynomial is: {lag_poly1}")
lag_poly2=sp.lambdify(x,lag_poly1,"numpy")
xp=float(input("Enter the value to interpolate: "))
int_value=lag_poly2(xp)
print(f"Interpolated value at {xp} is : {round(int_value,4)}")
w=np.linspace(min(X)-5,max(X)+5,1000)
plt.plot(w,lag_poly2(w),label="Lagrange Curve")
plt.scatter(X,Y,label="Data Points",color="green")
plt.scatter(xp,lag_poly2(xp),label="Interpolated values ",color="Orange")
plt.grid(True)
plt.legend()
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Lagrange Interpolation Method to Analyse Data")
plt.axhline(0)
plt.axvline(0)
plt.show()
    
                