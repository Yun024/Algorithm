import sys
input = sys.stdin.readline

n = int(input().strip())
ans = 0
for _ in range(n):
    s = input().strip()
    if int(s.split("-")[1]) <= 90:
        ans +=1
print(ans)