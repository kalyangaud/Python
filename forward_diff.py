import numpy as np

# Number of data points
n = int(input("Enter the number of data points: "))
x = list(map(float, input("Enter x values : ").split()))
y = list(map(float, input("Enter y values : ").split()))
diff = np.zeros((n, n))
for i in range(n):
    diff[i][0] = y[i]
for j in range(1, n):
    for i in range(n - j):
        diff[i][j] = diff[i + 1][j - 1] - diff[i][j - 1]
print("\nForward Difference Table:")
print("x\t", end="")
for i in range(n):
    print(f"Δ^{i}y\t", end="")
print()

for i in range(n):
    print(f"{x[i]}\t", end="")
    for j in range(n - i):
        print(f"{diff[i][j]:.4f}\t", end="")
    print()
h = x[1] - x[0]
for i in range(1, n - 1):
    if abs((x[i + 1] - x[i]) - h) > 1e-6:
        print("\nError: x values are not equally spaced.")
        exit()
xp = float(input("\nEnter the value of x to interpolate: "))
p = (xp - x[0]) / h
result = diff[0][0]
p_term = 1
fact = 1

for i in range(1, n):
    p_term *= (p - (i - 1))
    fact *= i
    result += (p_term * diff[0][i]) / fact

print(f"\nInterpolated value at x = {xp} is {result:.3f}")