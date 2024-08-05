def knapsack(weights, values, capacity):
    n = len(weights)
    ratio = [(values[i] / weights[i], weights[i], values[i]) for i in range(n)]
    ratio.sort(reverse=True, key=lambda x: x[0])

    total_value = 0
    for r in ratio:
        if capacity - r[1] >= 0:
            capacity -= r[1]
            total_value += r[2]
        else:
            total_value += r[0] * capacity
            break
    return total_value

weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
print("Maximum value in Knapsack =", knapsack(weights, values, capacity))
