import sys

n = int(sys.stdin.readline().strip())
cost = [list(map(int,i.split())) for i in sys.stdin.read().strip().split("\n")]

for i in range(1,n):
    for j in range(3):
        cost[i][j] += min(cost[i-1][k] for k in range(3) if j != k)

print(min(cost[-1]))