def minCoinsToAdd(coins, target):
    coins.sort()
    current_sum = 0
    additions = 0
    i = 0
    
    while current_sum < target:
        if i < len(coins) and coins[i] <= current_sum + 1:
            current_sum += coins[i]
            i += 1
        else:
            current_sum += current_sum + 1
            additions += 1
    return additions
coins1 = [1, 4, 10]
target1 = 19
print(minCoinsToAdd(coins1, target1))
coins2 = [1, 4, 10, 5, 7, 19]
target2 = 19
print(minCoinsToAdd(coins2, target2)) 
