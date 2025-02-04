import numpy as np

M = np.array([
    [1/4, 3/4, 0],
    [0, 1/4, 3/4],
    [3/4, 0, 1/4]
], dtype=float)

eigenvalues_numpy, eigenvectors = np.linalg.eig(M)

print("The Eigenvalues (LU):", eigenvalues_numpy)
print("\nThe Eigenvectors (NumPy):\n", eigenvectors)

# PDP^-1
P = eigenvectors
D = np.diag(eigenvalues_numpy)
P_inv = np.linalg.inv(P)

print("\nMatrix of passage P:\n", P)
print("\nDiagonal matrix D:\n", D)
print("\nInverse of P:\n", P_inv)

# Reconstruction of A using PDP^-1
A_reconstructed = np.dot(np.dot(P, D), P_inv)
print("\nReconstructed A (P * D * P^-1):\n", A_reconstructed)

# A^100
D_100 = np.diag(np.power(eigenvalues_numpy, 100))
A_100 = np.dot(np.dot(P, D_100), P_inv)
print("\nA^100:\n", A_100)
