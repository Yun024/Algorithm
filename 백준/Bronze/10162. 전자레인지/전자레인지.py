import sys

t = int(sys.stdin.readline().strip())
button = [300,60,10]
ans = []

for b in button:
    ans.append(t//b)
    t %= b

if t:
    print(-1)
else:
    print(*ans)