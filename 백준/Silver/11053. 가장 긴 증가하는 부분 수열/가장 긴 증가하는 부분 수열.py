import sys

input = sys.stdin.readline
n = int(input().strip())
nums = list(map(lambda x: int(x),sys.stdin.readline().split()))

def seq(n,nums):
    
    dp = [0] * n
    dp[0] = 1

    for i in range(1,n):
        max_n = 0
        for j in range(i-1,-1,-1):
            if nums[i] > nums[j]:
                max_n = max(max_n,dp[j])
        dp[i] = max_n + 1

    return max(dp)

print(seq(n,nums))