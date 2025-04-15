import sys

def make_one(n):
    
    if n == 1:
        return 0
    if n <= 3:
        return 1
    
    dp = [0] * (n+1)
    dp[2] = 1
    dp[3] = 1
    
    for i in range(4,n+1):

        score = dp[i-1]
        if i%3 == 0:
            score = min(score,dp[i//3])
            
        if i%2 == 0:
            score = min(score,dp[i//2])
        dp[i] = score + 1

    return dp[n]

n = int(sys.stdin.readline().strip())
print(make_one(n))
    