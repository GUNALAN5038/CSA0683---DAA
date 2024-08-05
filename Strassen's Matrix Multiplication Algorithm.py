def strassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    else:
        mid = n // 2

        A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]
        A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
        A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
        A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]

        B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
        B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
        B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
        B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

        P1 = strassen(A11, matrix_subtract(B12, B22))
        P2 = strassen(matrix_add(A11, A12), B22)
        P3 = strassen(matrix_add(A21, A22), B11)
        P4 = strassen(A22, matrix_subtract(B21, B11))
        P5 = strassen(matrix_add(A11, A22), matrix_add(B11, B22))
        P6 = strassen(matrix_subtract(A12, A22), matrix_add(B21, B22))
        P7 = strassen(matrix_subtract(A11, A21), matrix_add(B11, B12))

        C11 = matrix_add(matrix_subtract(matrix_add(P5, P4), P2), P6)
        C12 = matrix_add(P1, P2)
        C21 = matrix_add(P3, P4)
        C22 = matrix_subtract(matrix_subtract(matrix_add(P5, P1), P3), P7)

        C = [[0 for j in range(n)] for i in range(n)]
        for i in range(mid):
            for j in range(mid):
                C[i][j] = C11[i][j]
                C[i][j + mid] = C12[i][j]
                C[i + mid][j] = C21[i][j]
                C[i + mid][j + mid] = C22[i][j]

        return C

def matrix_add(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C

def matrix_subtract(A, B):
    n = len(A)
    C = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
matrices = [
    ([[1, 7], [3, 5]], [[6, 8], [4, 2]], [[34, 24], [38, 34]]),
]

for A, B, expected in matrices:
    print(f"Matrix A: {A}, Matrix B: {B}")
    result = strassen(A, B)
    print(f"Expected: {expected}, Output: {result}\n")
