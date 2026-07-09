import pandas as pd
import numpy as np

print("LU FACTORIZATION METHOD OF SOLVING SYSTEM OF LINEAR EQUATION")

n = int(input("Enter the number of variables in the system: "))

A = []
for i in range(0, n):     
    row = list(map(float,
                   input(f"Enter the row elements {i+1} of augmented matrix: ").split()))
    A.append(row)

A = np.array(A, dtype=float)
print(f"The augmented matrix is\n{A}\n")


C = A[:, :-1]
B = A[:, -1]

L = np.zeros((n, n))
U = np.zeros((n, n))

for i in range(0, n):     
    for j in range(0, n): 

        if i == 0:
            U[i, j] = C[i, j]

        if i == j:
            L[i, j] = 1

        if i != j and i < j:
            L[i, j] = 0

        if i != j and i > j:
            U[i, j] = 0

        if j == 0 and i >= 1:
            L[i, j] = C[i, j] / U[j, j]

        s = 0
        for k in range(0, j):
            if i >= 1 and j >= 1 and i <= j:
                s = s + L[i, k] * U[k, j]

        if i >= 1 and j >= 1 and i <= j:
            U[i, j] = C[i, j] - s

        S = 0
        for t in range(0, j):   
            if i >= 1 and j >= 1 and i > j:
                S = S + L[i, t] * U[t, j]   

        if i >= 1 and j >= 1 and i > j:
            L[i, j] = (C[i, j] - S) / U[j, j]  

print("The lower triangular matrix is L:")
print(L)

print("The upper triangular matrix is U:")
print(U)

V = np.linalg.solve(L, B)


x = np.linalg.solve(U, V)

print("Solution V of LV = B:")
print(V)

print("The required solution is:")
for i in range(n):
    print(f"x{i} = {x[i]}")