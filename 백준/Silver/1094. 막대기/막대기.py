import sys
n = int(sys.stdin.readline().strip())

ans = 0
while n:
    ans += n%2
    n = n//2
print(ans)