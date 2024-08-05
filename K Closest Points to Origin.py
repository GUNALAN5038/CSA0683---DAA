import heapq
import math

def k_closest(points, k):
    max_heap = []

    for (x, y) in points:
        dist = math.sqrt(x**2 + y**2)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist, (x, y)))
        else:
            heapq.heappushpop(max_heap, (-dist, (x, y)))

    return [point for (_, point) in max_heap]

# Test cases
points_cases = [
    ([[1, 3], [-2, 2], [5, 8], [0, 1]], 2, [[-2, 2], [0, 1]]),
    ([[1, 3], [-2, 2]], 1, [[-2, 2]]),
    ([[3, 3], [5, -1], [-2, 4]], 2, [[3, 3], [-2, 4]]),
]

for points, k, expected in points_cases:
    print(f"Points: {points}, K: {k}")
    closest_points = k_closest(points, k)
    print(f"Expected: {expected}, Output: {closest_points}\n")
