def three_assembly_lines(n, a1, a2, a3, t):
    dp = [[0] * n for _ in range(3)]
    dp[0][0] = a1[0]
    dp[1][0] = a2[0]
    dp[2][0] = a3[0]
    
    for i in range(1, n):
        dp[0][i] = a1[i] + min(dp[0][i-1], dp[1][i-1] + t[1][0], dp[2][i-1] + t[2][0])
        dp[1][i] = a2[i] + min(dp[1][i-1], dp[0][i-1] + t[0][1], dp[2][i-1] + t[2][1])
        dp[2][i] = a3[i] + min(dp[2][i-1], dp[0][i-1] + t[0][2], dp[1][i-1] + t[1][2])
    
    return min(dp[0][n-1], dp[1][n-1], dp[2][n-1])
n = 3
a1 = [5, 9, 3]
a2 = [6, 8, 4]
a3 = [7, 6, 5]
t = [
  [0, 2, 3],
  [2, 0, 4],
  [3, 4, 0]
]
print(f"Minimum time: {three_assembly_lines(n, a1, a2, a3, t)}")  
