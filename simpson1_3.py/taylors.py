import math

def taylor(x, n):
    s = 0
    for i in range(n):
        s += x**i / math.factorial(i)
    return s

x = float(input("Enter x: "))
n = int(input("Enter number of terms: "))

print("Taylor series value =", taylor(x, n))