import pandas as pd
import numpy as np

n=int(input("enter the number of variables of the system:"))
print("enter the augmented matrix using row-wise using space:")

A=[]

for i in range(n):
    row=list(map(float,input(f"enter the {i+1}th row: ").split()))
    A.append(row)
A=np.array(A,dtype=float)
print(f"the augmented matrix is \n {A}")

for i in range(n):
    if A[i,i]==0:
        for j in range(i+1,n):
            if A[j,i]!=0:
                A[[i,j]]=A[[j,i]]
    if A[i,i]!=0:
        A[i]=(A[i])/(A[i,i])
    else:
        print("matrix is singular,system is inconsistent")
        exit()
    for j in range(n):
        if j!=i:
            A[j]=A[j]-A[j,i]*A[i]

print(f"the normal matrix {A}")
x=A[:,-1]
print("required solution")

for i in range(n):
    print(f"x{i}={round(x[i],4)}")

    



