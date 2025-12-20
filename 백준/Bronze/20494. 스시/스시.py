import sys
input = sys.stdin.readline

n = int(input().strip())
ans = [0]*26
for _ in range(n):
    strings = input().strip()
    for s in strings:
        ans[ord(s)-65] += 1

print(sum(ans))