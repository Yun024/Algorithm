import sys

input = sys.stdin.readline
n,m = map(int,input().split())

dic = {}
for _ in range(n):
    i,j = input().split()
    dic[i] = int(j)

ans = 0
for _ in range(m):
    i,j = input().split()
    if dic[i]*1.05 < int(j):
        ans+=1

print(ans)