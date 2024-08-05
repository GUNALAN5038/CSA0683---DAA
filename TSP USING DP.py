from itertools import permutations

def travelling_salesman(graph, s):
    vertices = [i for i in range(len(graph)) if i != s]
    min_path = float('inf')
    next_permutation = permutations(vertices)

    for perm in next_permutation:
        current_pathweight = 0
        k = s
        for j in perm:
            current_pathweight += graph[k][j]
            k = j
        current_pathweight += graph[k][s]
        min_path = min(min_path, current_pathweight)

    return min_path

graph = [[0, 10, 15, 20],
         [10, 0, 35, 25],
         [15, 35, 0, 30],
         [20, 25, 30, 0]]
s = 0
print("Minimum cost of Travelling Salesman problem is", travelling_salesman(graph, s))
