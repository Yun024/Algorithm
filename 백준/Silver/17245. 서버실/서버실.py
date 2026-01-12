import sys
input = sys.stdin.readline

n = int(input().strip())
servers = [list(map(int,input().split())) for _ in range(n)]
total = sum([sum(i) for i in servers])
half = total//2 + 1 if total % 2 else total//2

right = max([max([j for j in i]) for i in servers])
left = 0

while left <= right:
    mid = (left+right)//2
    temp = 0
    for server in servers:
        for s in server:
            temp += min(s,mid)
    if temp >= half:
        ans = mid
        right = mid -1
    else:
        left = mid + 1

print(ans)
