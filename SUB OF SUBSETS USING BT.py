def sum_of_subsets(arr, target, subset=[], index=0):
    if target == 0:
        print(subset)
        return
    for i in range(index, len(arr)):
        if target >= arr[i]:
            sum_of_subsets(arr, target - arr[i], subset + [arr[i]], i + 1)

arr = list(map(int, input("Enter elements of the array: ").split()))
target = int(input("Enter the target sum: "))
print("Subsets with sum", target, "are:")
sum_of_subsets(arr, target)
