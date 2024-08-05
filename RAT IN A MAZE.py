def print_solution(sol):
    for row in sol:
        print(" ".join(str(cell) for cell in row))
    print()

def is_safe(maze, x, y):
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def solve_maze(maze):
    sol = [[0] * len(maze[0]) for _ in range(len(maze))]
    if not solve_maze_util(maze, 0, 0, sol):
        print("No solution exists")
        return False
    print_solution(sol)
    return True

def solve_maze_util(maze, x, y, sol):
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        sol[x][y] = 1
        return True
    if is_safe(maze, x, y):
        sol[x][y] = 1
        if solve_maze_util(maze, x + 1, y, sol):
            return True
        if solve_maze_util(maze, x, y + 1, sol):
            return True
        sol[x][y] = 0
        return False
    return False
maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]
solve_maze(maze)
