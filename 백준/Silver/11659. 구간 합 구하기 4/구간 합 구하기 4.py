import sys

input = sys.stdin.readline
n,m= map(int,input().split())
nums = list(map(int,input().split()))

def prefix_sum(n,nums):
    
    dp = [0]*n

    for i in range(n):
        dp[i] = dp[i-1] + nums[i]

    return dp

dp = prefix_sum(n,nums)

for i in range(m):
    x,y = map(int,input().split())
    print(dp[y-1]) if x-2 < 0 else print(dp[y-1] - dp[x-2])