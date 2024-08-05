def merge_sort_with_count(arr):
    global comparison_count
    comparison_count = 0

    def merge_sort(arr):
        if len(arr) <= 1:
            return arr

        mid = len(arr) // 2
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])

        return merge(left, right)

    def merge(left, right):
        global comparison_count
        sorted_arr = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparison_count += 1
            if left[i] < right[j]:
                sorted_arr.append(left[i])
                i += 1
            else:
                sorted_arr.append(right[j])
                j += 1

        sorted_arr.extend(left[i:])
        sorted_arr.extend(right[j:])

        return sorted_arr

    sorted_arr = merge_sort(arr)
    return sorted_arr, comparison_count
arrays = [
    ([12, 4, 78, 23, 45, 67, 89, 1], [1, 4, 12, 23, 45, 67, 78, 89]),
    ([38, 27, 43, 3, 9, 82, 10], [3, 9, 10, 27, 38, 43, 82]),
]

for arr, expected in arrays:
    print(f"Array: {arr}")
    sorted_arr, comparisons = merge_sort_with_count(arr)
    print(f"Expected: {expected}")
    print(f"Output: {sorted_arr}")
    print(f"Comparisons: {comparisons}\n")
