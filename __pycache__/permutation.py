def permutation(n, r):
    result = 1
    for i in range(r):
        result *= n - i
    return result

n = int(input("Enter n: "))
r = int(input("Enter r: "))

if r <= n:
    print("Permutation =", permutation(n, r))
else:
    print("r must be less than or equal to n ")/n
