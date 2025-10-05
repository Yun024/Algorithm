import sys
input = sys.stdin.readline

t = int(input().strip())
ans = 0
for _ in range(t):
    strings = input().strip()
    if strings[0] == 'C':
        ans += 1
print(ans)