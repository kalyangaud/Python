import sympy as sp

x = sp.symbols('x')
y = sp.Function('y')
P = sp.sympify(input("Enter P(x): "))
Q = sp.sympify(input("Enter Q(x): "))

# Define differential equation
eq = sp.Eq(sp.diff(y(x), x) + P*y(x), Q)
solution = sp.dsolve(eq)
print("Differential Equation:")
print(eq)
print("Solution:")
print(solution)