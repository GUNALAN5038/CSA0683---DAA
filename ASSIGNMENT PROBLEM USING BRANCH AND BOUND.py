import numpy as np

def branch_and_bound(cost):
    n = len(cost)
    row_ind, col_ind = np.zeros(n, dtype=int), np.zeros(n, dtype=int)
    assignment = np.zeros(n, dtype=int)
    total_cost = 0

    for i in range(n):
        row_ind[i] = np.argmin(cost[i])
        total_cost += cost[i][row_ind[i]]

    for j in range(n):
        col_ind[j] = np.argmin(cost[:, j])
        total_cost += cost[col_ind[j]][j]

    for i in range(n):
        for j in range(n):
            if row_ind[i] == col_ind[j]:
                assignment[i] = j

    return total_cost, assignment

cost = np.array([[82, 83, 69, 92],
                 [77, 37, 49, 92],
                 [11, 69, 5, 86],
                 [8, 9, 98, 23]])
total_cost, assignment = branch_and_bound(cost)
print("Total cost of assignment:", total_cost)
print("Assignment of tasks:", assignment)
