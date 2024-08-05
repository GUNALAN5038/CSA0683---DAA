def median_of_medians(arr, k):
    if len(arr) < 10:
        return sorted(arr)[k-1]

    sublists = [arr[j:j+5] for j in range(0, len(arr), 5)]
    medians = [sorted(sublist)[len(sublist)//2] for sublist in sublists]
    
    pivot = median_of_medians(medians, len(medians)//2 + 1)
    
    low = [el for el in arr if el < pivot]
    high = [el for el in arr if el > pivot]
    
    k_index = k - 1
    if k_index < len(low):
        return median_of_medians(low, k)
    elif k_index < len(arr) - len(high):
        return pivot
    else:
        return median_of_medians(high, k - (len(arr) - len(high)))
arrays = [
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 6, 6),
    ([23, 17, 31, 44, 55, 21, 20, 18, 19, 27], 5, 20),
]

for arr, k, expected in arrays:
    print(f"Array: {arr}, K: {k}")
    result = median_of_medians(arr, k)
    print(f"Expected: {expected}, Output: {result}\n")
