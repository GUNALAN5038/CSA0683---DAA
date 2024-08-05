def optimal_cost(matrix, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])
    return matrix

cost_matrix = [[0, 3, float('inf'), 7],
               [8, 0, 2, float('inf')],
               [5, float('inf'), 0, 1],
               [2, float('inf'), float('inf'), 0]]
n = len(cost_matrix)
print("Optimal cost matrix is:")
optimal_matrix = optimal_cost(cost_matrix, n)
for row in optimal_matrix:
    print(row)
