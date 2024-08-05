def karatsuba(x, y):
    if x < 10 or y < 10:
        return x * y

    n = max(len(str(x)), len(str(y)))
    m = n // 2

    x_high = x // 10**m
    x_low = x % 10**m
    y_high = y // 10**m
    y_low = y % 10**m

    z0 = karatsuba(x_low, y_low)
    z1 = karatsuba((x_low + x_high), (y_low + y_high))
    z2 = karatsuba(x_high, y_high)

    return (z2 * 10**(2*m)) + ((z1 - z2 - z0) * 10**m) + z0

# Test cases
cases = [
    (1234, 5678, 7016652),
]

for x, y, expected in cases:
    print(f"X: {x}, Y: {y}")
    result = karatsuba(x, y)
    print(f"Expected: {expected}, Output: {result}\n")
