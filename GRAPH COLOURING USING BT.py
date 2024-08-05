def is_safe(graph, color):
    for i in range(len(graph)):
        for j in range(i + 1, len(graph)):
            if graph[i][j] and color[j] == color[i]:
                return False
    return True

def graph_coloring(graph, m, i, color):
    if i == len(graph):
        return True
    for j in range(1, m + 1):
        color[i] = j
        if is_safe(graph, color):
            if graph_coloring(graph, m, i + 1, color):
                return True
        color[i] = 0
    return False

def graph_coloring_util(graph, m):
    color = [0] * len(graph)
    if not graph_coloring(graph, m, 0, color):
        print("Solution does not exist")
    else:
        print("Colors assigned to vertices:", color)

graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
m = 3
graph_coloring_util(graph, m)
