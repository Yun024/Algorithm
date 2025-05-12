import sys

input = sys.stdin.readline
n = int(input().strip())
dist = list(map(int,input().split()))
oil_cost = list(map(int,input().split()))

dp = [0] * len(oil_cost)
dp[1] = dist[0] * oil_cost[0]
min_cost = oil_cost[0]

for i in range(2,len(oil_cost)):
    min_cost = min(min_cost,oil_cost[i-1])
    dp[i] = dp[i-1] + min_cost * dist[i-1]

print(dp[-1])




