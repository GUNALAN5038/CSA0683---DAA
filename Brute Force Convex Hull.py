def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def convex_hull(points):
    hull = []
    n = len(points)
    if n < 3:
        return hull
    
    l = 0
    for i in range(1, n):
        if points[i][0] < points[l][0]:
            l =
