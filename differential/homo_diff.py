import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')

a = float(input("Enter coefficient of y'': "))
b = float(input("Enter coefficient of y': "))
c = float(input("Enter coefficient of y: "))

eq = sp.Eq(a*sp.diff(y(x), x, 2) +
           b*sp.diff(y(x), x) +
           c*y(x), 0)

solution = sp.dsolve(eq)
print("\nDifferential Equation:")
print(eq)
print("\nSolution:")
print(solution)