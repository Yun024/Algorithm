import sys
input = sys.stdin.readline

n,m = map(int,input().split())
N = list(map(int,input().split()))
M = list(map(int,input().split()))

ans = sum(N)
for i in M:
    if i:
        ans *= i
print(ans)

