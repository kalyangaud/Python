import sympy as sp

x, y = sp.symbols('x y')

def partial_derivative(f):
    dx = sp.diff(f, x)
    dy = sp.diff(f, y)
    return dx, dy

f = x**2 + x*y + y**2
dx, dy = partial_derivative(f)

print("Function:", f)
print("Partial derivative with respect to x:", dx)
print("Partial derivative with respect to y:", dy)