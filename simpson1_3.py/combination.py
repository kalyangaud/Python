def combination(n, r):
    result = 1
    for i in range(1, r + 1):
        result = result * (n - i + 1) // i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r <= n:
    print("Combination =", combination(n, r))
else:
    print("r must be less than or equal to n")