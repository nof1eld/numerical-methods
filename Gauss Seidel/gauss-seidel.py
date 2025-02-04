def gauss_seidel(A, b, x, iterations):
    for i in range(len(A)):
        if A[i][i] == 0:
            print("The diagonal element A is zero.")
            return

    l = 0
    if abs(A[l][l]) < abs(A[l][1]) + abs(A[l][2]):
        print("The condition of diagonal dominance is not satisfied in row 0")
        return
    else:
        l =l+ 1

    if abs(A[l][l]) < abs(A[l][0]) + abs(A[l][2]):
        print("The condition of diagonal dominance is not satisfied in row 1")
        return
    else:
        l = l+1

    if abs(A[l][l]) < abs(A[l][0]) + abs(A[l][1]):
        print("The condition of diagonal dominance is not satisfied in row 2")
        return
    else:
        for m in range(iterations):
            x_new = x
            for i in range(len(A)):
                sum1 = 0
                sum2 = 0
                for j in range(i):
                    if j != i:
                        sum1 =sum1+ A[i][j] * x_new[j]
                for j in range(i+1, len(A)):
                    if j != i:
                        sum2 =sum2+ A[i][j] * x[j]
                        
                x_new[i] = (b[i] - sum1 - sum2) / A[i][i]
            x = x_new
        return x



A = [[5, -2, 3],
     [-3, 9, 1],
     [2, -1, -7]]
b = [-1, 2, 3]
x_0 = [0, 0, 0]


solution = gauss_seidel(A, b, x_0, iterations=7)
print("Solution:", solution)