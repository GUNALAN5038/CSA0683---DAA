def gray_code(n):
    result = []
    
    def backtrack(path):
        if len(path) == n:
            result.append(int("".join(map(str, path)), 2))
            return
        path.append(0)
        backtrack(path)
        path.pop()
        path.append(1)
        backtrack(path)
        path.pop()
    
    backtrack([])
    return result
n = 2
print(gray_code(n)) 
