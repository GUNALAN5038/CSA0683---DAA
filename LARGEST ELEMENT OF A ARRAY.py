def largest_element(arr):
    return max(arr)

arr = list(map(int, input("Enter elements of the array: ").split()))
print("Largest element is", largest_element(arr))
