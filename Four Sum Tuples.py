def four_sum_count(A, B, C, D):
    AB_sum = {}
    for a in A:
        for b in B:
            if a + b in AB_sum:
                AB_sum[a + b] += 1
            else:
                AB_sum[a + b] = 1

    count = 0
    for c in C:
        for d in D:
            if -(c + d) in AB_sum:
                count += AB_sum[-(c + d)]
    
    return count
cases = [
    ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
    ([0], [0], [0], [0], 1),
]

for A, B, C, D, expected in cases:
    print(f"A: {A}, B: {B}, C: {C}, D: {D}")
    result = four_sum_count(A, B, C, D)
    print(f"Expected: {expected}, Output: {result}\n")
