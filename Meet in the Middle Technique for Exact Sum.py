def meet_in_the_middle_exact(arr, exact_sum):
    from itertools import combinations

    n = len(arr)
    first_half = arr[:n//2]
    second_half = arr[n//2:]

    first_half_sums = {}
    for r in range(len(first_half) + 1):
        for combo in combinations(first_half, r):
            s = sum(combo)
            first_half_sums[s] = combo

    for r in range(len(second_half) + 1):
        for combo in combinations(second_half, r):
            s = sum(combo)
            remain = exact_sum - s
            if remain in first_half_sums:
                return True

    return False
cases = [
    ([1, 3, 9, 2, 7, 12], 15),
    ([3, 34, 4, 12, 5, 2], 15),
]

for arr, exact_sum in cases:
    print(f"Array: {arr}, Exact Sum: {exact_sum}")
    result = meet_in_the_middle_exact(arr, exact_sum)
    print(f"Subset Exists: {result}\n")
