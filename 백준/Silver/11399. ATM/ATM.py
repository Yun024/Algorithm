import sys

input = sys.stdin.readline 
n = int(input().strip())
num_list = sorted(map(int,input().split()))

dp = [0] * n
dp[0] = num_list[0]

for i in range(1,n):
    dp[i] = dp[i-1] + num_list[i]

print(sum(dp))

