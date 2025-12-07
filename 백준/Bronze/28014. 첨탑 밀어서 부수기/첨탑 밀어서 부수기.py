import sys

n = int(sys.stdin.readline().strip())
towers = list(map(int,sys.stdin.readline().split()))

ans = 0
temp = 0
for idx,val in enumerate(towers):
    if temp <= val:
        ans += 1
    temp = val
print(ans)