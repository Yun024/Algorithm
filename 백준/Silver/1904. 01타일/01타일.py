def tile(n):
    if n <= 3:
        return n
    
    dp = [0] * (n+1)
    dp[0] = 1
    dp[1] = 1
    
    for i in range(2, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
    return dp[n]

n = int(input())
print(tile(n))