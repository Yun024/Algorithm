import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = [[0]*(m+1)] + [[0]+ list(map(int,input().split())) for _ in range(n)]
prefix_sum = [[0]*(m+1) for _ in range(n+1)]
for x in range(1,n+1):
    for y in range(1,m+1):
        prefix_sum[x][y] = prefix_sum[x-1][y] + prefix_sum[x][y-1] + array[x][y] - prefix_sum[x-1][y-1]

k = int(input().strip())
for _ in range(k):
    i,j,x,y = map(int,input().split())
    print(prefix_sum[x][y] - prefix_sum[i-1][y] - prefix_sum[x][j-1] + prefix_sum[i-1][j-1])