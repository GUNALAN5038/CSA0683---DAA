def min_max_sequence(arr):
    min_val = min(arr)
    max_val = max(arr)
    return min_val, max_val

arr = list(map(int, input("Enter elements of the array: ").split()))
min_val, max_val = min_max_sequence(arr)
print("Minimum value:", min_val)
print("Maximum value:", max_val)
