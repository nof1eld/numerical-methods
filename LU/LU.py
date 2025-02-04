import numpy as np

def FactLU(matrix):
    N = len(A)
    L = np.zeros((N, N))
    U = np.zeros((N, N))
    for i in range(N):
        L[i][i] = 1
    for j in range(N):
        U[0][j] = A[0][j]
    for i in range(1, N):
        L[i][0] = A[i][0] / U[0][0]
    for i in range(1, N):
        for j in range(i, N):
            sum1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum1
        for j in range(i+1, N):
            sum2 = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - sum2) / U[i][i]
            
    return L, U

A = np.array([
    [0, 0, 0],
    [1, 0, 2],
    [0, 1, 0]
])

L, U = FactLU(A)
print("Matrix L =")
print(L)
print("\nMatrix U =")
print(U)