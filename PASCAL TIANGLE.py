def pascal_triangle(n):
    result = []
    for i in range(n):
        row = [1]
        if result:
            last_row = result[-1]
            row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
            row.append(1)
        result.append(row)
    return result

n = int(input("Enter the number of rows: "))
triangle = pascal_triangle(n)
for row in triangle:
    print(row)
