def sum_of_digits(n):
    return sum(map(int, str(n)))

num = int(input("Enter a number: "))
print("Sum of digits is", sum_of_digits(num))
