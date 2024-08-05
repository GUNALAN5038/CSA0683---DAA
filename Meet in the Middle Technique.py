def meet_in_the_middle(arr, target_sum):
    from itertools import combinations

    n = len(arr)
    first_half = arr[:n//2]
    second_half = arr[n//2:]

    first_half_sums = {}
    for r in range(len(first_half) + 1):
        for combo in combinations(first_half, r):
            s = sum(combo)
            first_half_sums[s] = combo

    closest_sum = None
    closest_set = None

    for r in range(len(second_half) + 1):
        for combo in combinations(second_half, r):
            s = sum(combo)
            remain = target_sum - s
            if remain in first_half_sums:
                if closest_sum is None or abs(target_sum - closest_sum) > abs(target_sum - (s + remain)):
                    closest_sum = s + remain
                    closest_set = first_half_sums[remain] + combo

    return closest_set

cases = [
    ([45, 34, 4, 12, 5, 2], 42),
    ([1, 3, 2, 7, 4, 6], 10),
]

for arr, target in cases:
    print(f"Array: {arr}, Target Sum: {target}")
    result = meet_in_the_middle(arr, target)
    print(f"Closest Subset: {result}, Sum: {sum(result)}\n")
