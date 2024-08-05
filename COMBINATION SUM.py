def combination_sum(candidates, target):
    result = []
    
    def backtrack(start, target, path):
        if target == 0:
            result.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > target:
                continue
            path.append(candidates[i])
            backtrack(i, target - candidates[i], path)
            path.pop()
    
    backtrack(0, target, [])
    return result
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  
