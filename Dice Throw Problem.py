def dice_throw(num_sides, num_dice, target):
    dp = [[0] * (target + 1) for _ in range(num_dice + 1)]
    dp[0][0] = 1
    for dice in range(1, num_dice + 1):
        for t in range(1, target + 1):
            for k in range(1, num_sides + 1):
                if t - k >= 0:
                    dp[dice][t] += dp[dice - 1][t - k]
    
    return dp[num_dice][target]
print(f"Number of ways to reach sum 7: {dice_throw(6, 2, 7)}") 
print(f"Number of ways to reach sum 10: {dice_throw(4, 3, 10)}") 
