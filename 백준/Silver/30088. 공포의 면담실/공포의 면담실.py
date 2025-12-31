import sys
input = sys.stdin.readline

t = int(input().strip())
times = [sum(list(map(int,input().split()))[1:]) for _ in range(t)]
dp = [0]*(t+1)
times.sort()

for i in range(1,t+1):
    dp[i] = dp[i-1] + times[i-1]

print(sum(dp))