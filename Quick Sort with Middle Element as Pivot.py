def quick_sort_middle(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid_index = len(arr) // 2
        pivot = arr[mid_index]
        less_than_pivot = [x for x in arr[:mid_index] + arr[mid_index+1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[:mid_index] + arr[mid_index+1:] if x > pivot]
        return quick_sort_middle(less_than_pivot) + [pivot] + quick_sort_middle(greater_than_pivot)
arrays = [
    ([19, 72, 35, 46, 58, 91, 22, 31], [19, 22, 31, 35, 46, 58, 72, 91]),
    ([31, 23, 35, 27, 11, 21, 15, 28], [11, 15, 21, 23, 27, 28, 31, 35]),
]

for arr, expected in arrays:
    print(f"Array: {arr}")
    sorted_arr = quick_sort_middle(arr)
    print(f"Expected: {expected}")
    print(f"Output: {sorted_arr}\n")
