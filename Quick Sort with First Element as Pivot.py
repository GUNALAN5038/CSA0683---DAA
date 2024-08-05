def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)
arrays = [
    ([10, 16, 8, 12, 15, 6, 3, 9, 5], [3, 5, 6, 8, 9, 10, 12, 15, 16]),
    ([12, 4, 78, 23, 45, 67, 89, 1], [1, 4, 12, 23, 45, 67, 78, 89]),
]

for arr, expected in arrays:
    print(f"Array: {arr}")
    sorted_arr = quick_sort(arr)
    print(f"Expected: {expected}")
    print(f"Output: {sorted_arr}\n")
