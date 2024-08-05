def partition(arr, low, high, pivot):
    pivot_value = arr[pivot]
    arr[pivot], arr[high] = arr[high], arr[pivot]
    store_index = low
    for i in range(low, high):
        if arr[i] < pivot_value:
            arr[i], arr[store_index] = arr[store_index], arr[i]
            store_index += 1
    arr[store_index], arr[high] = arr[high], arr[store_index]
    return store_index

def select(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = (low + high) // 2
    pivot_index = partition(arr, low, high, pivot_index)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return select(arr, low, pivot_index - 1, k)
    else:
        return select(arr, pivot_index + 1, high, k)

def kth_smallest(arr, k):
    return select(arr, 0, len(arr) - 1, k - 1)
cases = [
    ([12, 3, 5, 7, 19], 2, 5),
    ([12, 3, 5, 7, 4, 19, 26], 3, 5),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 6),
]

for arr, k, expected in cases:
    print(f"Array: {arr}, K: {k}")
    result = kth_smallest(arr, k)
    print(f"Expected: {expected}, Output: {result}\n")
