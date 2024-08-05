def insert_number(arr, num):
    arr.append(num)
    return sorted(arr)

arr = list(map(int, input("Enter elements of the array: ").split()))
num = int(input("Enter the number to insert: "))
print("Array after insertion:", insert_number(arr, num))
