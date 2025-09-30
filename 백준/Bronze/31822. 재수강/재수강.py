import sys
input = sys.stdin.readline

ans = input().strip()
t = int(input().strip())
res = 0
for _ in range(t):
    s = input().strip()
    if ans[:5] == s[:5]:
        res += 1
print(res)