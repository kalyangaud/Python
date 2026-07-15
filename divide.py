# Newton's Divided Difference Interpolation Method

n = int(input("Enter the number of data points: "))

x = []
y = []

print("Enter the x and y values:")
for i in range(n):
    xi, yi = map(float, input(f"Point {i+1} (x y): ").split())
    x.append(xi)
    y.append(yi)
dd = [[0 for _ in range(n)] for _ in range(n)]

# First column is y-values
for i in range(n):
    dd[i][0] = y[i]
for j in range(1, n):
    for i in range(n - j):
        dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i])
print("\nDivided Difference Table:")
for i in range(n):
    for j in range(n - i):
        print(f"{dd[i][j]:10.6f}", end="\t")
    print()
xp = float(input("\nEnter the value of x to interpolate: "))
yp = dd[0][0]
product = 1

for i in range(1, n):
    product *= (xp - x[i - 1])
    yp += product * dd[0][i]

print(f"\nInterpolated value at x = {xp} is {yp:.6f}")