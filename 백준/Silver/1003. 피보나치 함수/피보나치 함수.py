import sys
input = sys.stdin.readline

def list_sum(a,b):
    return [a[0]+b[0], a[1]+b[1]]

def pibo(n):
    
    dp = [[]] * (n+2)
    dp[0] = [1,0]
    dp[1] = [0,1]
    for i in range(2,n+1):
        dp[i] = list_sum(dp[i-1],dp[i-2])
    return dp[n]

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    print(*pibo(n))