def find_max_min(arr):
    if not arr:
        return None, None

    max_val = arr[0]
    min_val = arr[0]

    for num in arr[1:]:
        if num > max_val:
            max_val = num
        if num < min_val:
            min_val = num

    return min_val, max_val
arrays = [
    ([5, 7, 3, 4, 9, 12, 6, 2], (2, 12)),
    ([1, 3, 5, 7, 9, 11, 13, 15, 17], (1, 17)),
    ([22, 34, 35, 36, 43, 67, 12, 13, 15, 17], (12, 67)),
]
for arr, expected in arrays:
    print(f"Array: {arr}")
    min_val, max_val = find_max_min(arr)
    print(f"Expected: Min = {expected[0]}, Max = {expected[1]}")
    print(f"Output: Min = {min_val}, Max = {max_val}\n")
