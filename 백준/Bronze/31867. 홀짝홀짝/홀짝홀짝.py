import sys
input = sys.stdin.readline

t = int(input().strip())
strings = input().strip()

ans = 0
for s in strings:
    if int(s)%2:
        ans -= 1
    else:
        ans += 1

print(-1 if not ans else 0 if ans > 0 else 1)

