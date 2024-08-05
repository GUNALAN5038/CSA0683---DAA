def find_kth_missing(arr, k):
    missing = []
    current = 1
    idx = 0
    while len(missing) < k:
        if idx < len(arr) and arr[idx] == current:
            idx += 1
        else:
            missing.append(current)
        current += 1
    return missing[-1]

# Test Cases
print(find_kth_missing([2, 3, 4, 7, 11], 5)) 
print(find_kth_missing([1, 2, 3, 4], 2))  
