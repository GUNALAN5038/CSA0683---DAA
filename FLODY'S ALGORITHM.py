def floyd_warshall(graph):
    n = len(graph)
    dist = list(map(lambda i: list(map(lambda j: j, i)), graph))

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

graph = [[0, 3, float('inf'), 7],
         [8, 0, 2, float('inf')],
         [5, float('inf'), 0, 1],
         [2, float('inf'), float('inf'), 0]]
distances = floyd_warshall(graph)
print("Shortest distances between every pair of vertices:")
for row in distances:
    print(row)
