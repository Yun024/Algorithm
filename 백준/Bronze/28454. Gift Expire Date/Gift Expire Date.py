import sys
input = sys.stdin.readline

now = list(map(int,input().split("-")))
t = int(input().strip())
ans = 0
for _ in range(t):
    future = list(map(int,input().split("-")))
    if now <= future:
        ans += 1
print(ans)