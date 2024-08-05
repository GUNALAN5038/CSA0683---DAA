def can_partition_k_subsets(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem or max(nums) > target:
        return False
    
    def backtrack(groups):
        if not nums:
            return True
        v = nums.pop()
        for i in range(k):
            if groups[i] + v <= target:
                groups[i] += v
                if backtrack(groups):
                    return True
                groups[i] -= v
            if not groups[i]:
                break
        nums.append(v)
        return False
    
    nums.sort()
    return backtrack([0] * k)
nums = [4, 3, 2, 3, 5, 2, 1]
k = 4
print(can_partition_k_subsets(nums, k)) 
