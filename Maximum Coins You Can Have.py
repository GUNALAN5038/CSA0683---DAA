def maxCoins(piles):
    piles.sort()
    n = len(piles) // 3
    return sum(piles[n::2])
piles1 = [2, 4, 1, 2, 7, 8]
print(maxCoins(piles1))  
piles2 = [2, 4, 5]
print(maxCoins(piles2))
