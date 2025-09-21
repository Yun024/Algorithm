import sys
input = sys.stdin.readline

jinho = input().strip()
n = int(input().strip())
ans = 0

for _ in range(n):
    if input().strip() == jinho:
        ans += 1

print(ans)