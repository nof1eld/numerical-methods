import numpy as np

A = np.array([
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)


def gauss(A, B):
    N = len(B)
    X = np.zeros(N)
    
    
        for i in range(N - 1):
            for j in range(i + 1, N):
                f = A[j][i]/A[i][i]
                for k in range(N):
                    A[j][k] = A[j][k] - f * A[i][k]
                B[j] = B[j] - f * B[i]
    

        for i in range(N-1, -1, -1):
            S = B[i]
            for j in range(i + 1, N):
                S = S - A[i][j] * X[j]
            X[i] = S / A[i][i]
        return X


print("Solution:", gauss(A, B))