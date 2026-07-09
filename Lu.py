import numpy as np
np.set_printoptions(suppress=True,precision=3)
# -------------------------
# Initialization Phase
# -------------------------
print("\nLU FACTORIZATION METHOD FOR SOLVING SYSTEM OF LINEAR EQUATIONS")

n = int(input("Enter the number of variables: "))

A = []

print("\nEnter the augmented matrix row-wise:")
for i in range(n):
    row = list(map(float, input(f"Row {i+1}: ").split()))
    A.append(row)

A = np.array(A)

print("\nAugmented Matrix:")
print(A)

# Separate coefficient matrix and RHS vector
Coeff = A[:, :-1]
B = A[:, -1]

# -------------------------
# Matrix Initialization
# -------------------------
L = np.zeros((n, n))
U = np.zeros((n, n))

# -------------------------
# LU Decomposition
# (Doolittle Method)
# -------------------------
for i in range(n):

    # Compute Upper Triangular Matrix U
    for j in range(i, n):
        s = 0
        for k in range(i):
            s += L[i][k] * U[k][j]
        U[i][j] = Coeff[i][j] - s

    # Set diagonal of L = 1
    L[i][i] = 1

    # Compute Lower Triangular Matrix L
    for j in range(i + 1, n):
        s = 0
        for k in range(i):
            s += L[j][k] * U[k][i]

        if U[i][i] == 0:
            print("LU Factorization not possible (Zero Pivot).")
            exit()

        L[j][i] = (Coeff[j][i] - s) / U[i][i]

# -------------------------
# Display L and U
# -------------------------
print("\nLower Triangular Matrix L:")
print(L)

print("\nUpper Triangular Matrix U:")
print(U)

# -------------------------
# Forward Substitution
# Solve LV = B
# -------------------------
V = np.zeros(n)

for i in range(n):
    s = 0
    for j in range(i):
        s += L[i][j] * V[j]
    V[i] = (B[i] - s) / L[i][i]

print("\nSolution of LV = B")
for i in range(n):
    print(f"V{i+1} = {V[i]:.4f}")

# -------------------------
# Backward Substitution
# Solve UX = V
# -------------------------
X = np.zeros(n)

for i in range(n - 1, -1, -1):
    s = 0
    for j in range(i + 1, n):
        s += U[i][j] * X[j]

    X[i] = (V[i] - s) / U[i][i]
print("\nRequired Solution:")
for i in range(n):
    print(f"x{i} = {X[i]:.4f}")