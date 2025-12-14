import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = [0]*n
for _ in range(m):
    k,s,e = map(int,input().split())
    if ans[k-1] <= s:
        print("YES")
        ans[k-1] = e
    else:
        print("NO")