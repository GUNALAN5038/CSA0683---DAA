import heapq

def prim_mst(graph):
    start_vertex = 0
    visited = set()
    min_heap = [(0, start_vertex)]
    total_cost = 0

    while min_heap:
        cost, vertex = heapq.heappop(min_heap)
        if vertex not in visited:
            visited.add(vertex)
            total_cost += cost

            for next_vertex, weight in graph[vertex]:
                if next_vertex not in visited:
                    heapq.heappush(min_heap, (weight, next_vertex))

    return total_cost

graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}
print("Total cost of MST:", prim_mst(graph))
