def reverse_number(num):
    return int(str(num)[::-1])

num = int(input("Enter a number: "))
print("Reversed number is", reverse_number(num))
