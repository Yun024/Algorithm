import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()
ans = []

for k in ['u','s','o','p','c']:
    ans.append(strings.count(k))

print(min(ans))