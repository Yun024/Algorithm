import sys

fir = list(sys.stdin.readline().strip())
sec = list(sys.stdin.readline().strip())

dp = [[0] * (len(fir)+1) for i in range(len(sec)+1)]

for j,i in enumerate(sec):
    for n,m in enumerate(fir):
        if i == m:
            dp[j+1][n+1] = dp[j][n] + 1
        else:
            dp[j+1][n+1] = max(dp[j+1][n],dp[j][n+1])

print(dp[-1][-1])
