import sys
input = sys.stdin.readline

n = int(input().strip())
seat = list(input().strip())

ans = 1
while seat:
    temp = seat.pop()
    if temp == "L":
        seat.pop()
    ans += 1

if ans > n:
    print(n)
else:
    print(ans)