def jacobi(A, b, x, d):
    
    for i in range(len(A)):
        if A[i][i] == 0:
            print("The diagonal element A is zero.")
            return

    l = 0
    if abs(A[l][l]) < abs(A[l][1]) + abs(A[l][2]):
        print("The condition of diagonal dominance is not satisfied in row 1")
        return
    else:
        l =l+ 1

    if abs(A[l][l]) < abs(A[l][0]) + abs(A[l][2]):
        print("The condition of diagonal dominance is not satisfied in row 2")
        return
    else:
        l = l+1

    if abs(A[l][l]) < abs(A[l][0]) + abs(A[l][1]):
        print("The condition of diagonal dominance is not satisfied in row 3")
        return
    else:
            for t in range(d):
                for i in range(len(A)):
                    sum = 0 
                    for j in range(len(A)):
                        if j != i:
                          sum = sum+A[i][j] * x[j]
                    x[i] = (b[i] - sum) / A[i][i]
            return x
    
    
                              
A = [[5, -2, 3],
     [-3, 9, 1],
     [2, -1, -7]]
b = [-1, 2, 3]
x_0 = [0, 0, 0]

print("Solution:",jacobi(A, b, x_0, d=7) )
