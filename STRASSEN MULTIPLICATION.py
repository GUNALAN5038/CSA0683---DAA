import numpy as np

def strassen(X, Y):
    if X.shape[0] == 1:
        return X * Y
    else:
        mid = X.shape[0] // 2
        A, B, C, D = X[:mid, :mid], X[:mid, mid:], X[mid:, :mid], X[mid:, mid:]
        E, F, G, H = Y[:mid, :mid], Y[:mid, mid:], Y[mid:, :mid], Y[mid:, mid:]

        P1 = strassen(A, F - H)
        P2 = strassen(A + B, H)
        P3 = strassen(C + D, E)
        P4 = strassen(D, G - E)
        P5 = strassen(A + D, E + H)
        P6 = strassen(B - D, G + H)
        P7 = strassen(A - C, E + F)

        top_left = P5 + P4 - P2 + P6
        top_right = P1 + P2
        bottom_left = P3 + P4
        bottom_right = P1 + P5 - P3 - P7

        top = np.hstack((top_left, top_right))
        bottom = np.hstack((bottom_left, bottom_right))
        return np.vstack((top, bottom))

A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(strassen(A, B))
