import sys
input = sys.stdin.readline

n,k = map(int,input().split())
ans = [[0]*(i+1) for i in range(n)]
for i in range(len(ans)):
    ans[i][0] = 1
    ans[i][-1] = 1

for i in range(2,n):
    for x in range(i):
        if not ans[i][x]:
            ans[i][x] = ans[i-1][x-1] + ans[i-1][x]
print(ans[n-1][k-1])