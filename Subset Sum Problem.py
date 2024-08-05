def subset_sum(arr, target_sum):
    result = []
    
    def backtrack(start, current_sum, path):
        if current_sum == target_sum:
            result.append(path[:])
            return
        if current_sum > target_sum:
            return
        for i in range(start, len(arr)):
            path.append(arr[i])
            backtrack(i + 1, current_sum + arr[i], path)
            path.pop()
    
    backtrack(0, 0, [])
    return result

arr = [2, 3, 6, 7]
target_sum = 7
print(subset_sum(arr, target_sum))  
