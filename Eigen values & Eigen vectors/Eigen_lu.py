import numpy as np

def decomposition_LU(M):
    n = len(M)
    U = np.zeros((n, n))
    L = np.identity(n)

    if M.shape[0] != M.shape[1]:  
        print("Matrix A must be square.")  
        return -1 

    if np.any(np.diag(M) == 0):  
        print("Matrix A contains zero diagonal elements; division by zero will occur.")
        return -1

    M_copy = M.copy()

    for i in range(0, n):
        for j in range(i + 1, n):
            L[j][i] = M_copy[j][i] / M_copy[i][i]

        for j in range(i, n):
            U[i][j] = M_copy[i][j]    

        for j in range(i + 1, n):
            for k in range(i + 1, n):
                M_copy[j][k] -= L[j][i] * U[i][k]    

        U[i][i] = M_copy[i][i]
    
    return L, U

def eigen_values(M):
    A = M.copy()
    for i in range(1000):
        L, U = decomposition_LU(A)
        A_next = np.dot(U, L)
        if np.allclose(A, A_next, atol=1e-10):  # Check for convergence
            break
        A = A_next
    return np.diag(A)  # Eigenvalues

M = np.array([
    [1/4, 3/4, 0],
    [0, 1/4, 3/4],
    [3/4, 0, 1/4]
], dtype=float)

eigenvalues_lu = eigen_values(M)
eigenvalues_numpy, eigenvectors = np.linalg.eig(M)

print("The Eigenvalues (LU):", eigenvalues_lu)
print("\nThe Eigenvectors (NumPy):\n", eigenvectors)

# PDP^-1
P = eigenvectors
D = np.diag(eigenvalues_lu)
P_inv = np.linalg.inv(P)

print("\nMatrix of passage P:\n", P)
print("\nDiagonal matrix D:\n", D)
print("\nInverse of P:\n", P_inv)

# Reconstruction of A using PDP^-1
A_reconstructed = np.dot(np.dot(P, D), P_inv)
print("\nReconstructed A (P * D * P^-1):\n", A_reconstructed)

# A^100
D_100 = np.diag(np.power(eigenvalues_lu, 100))
A_100 = np.dot(np.dot(P, D_100), P_inv)
print("\nA^100:\n", A_100)
