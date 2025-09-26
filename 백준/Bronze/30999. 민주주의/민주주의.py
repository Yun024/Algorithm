import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = 0 
for _ in range(n):
    temp = input().strip()
    if temp.count('O') >= m//2+1:
        ans += 1
print(ans)
