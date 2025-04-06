def triangle(n):
    if n <= 3:
        return 1
    elif n <=5:
        return 2
    
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2
    dp[5] = 2
    
    for i in range(6,n+1):
        dp[i] = dp[i-1] + dp[i-5]

    return dp[n]

n = int(input())
for i in range(n):
    print(triangle(int(input())))