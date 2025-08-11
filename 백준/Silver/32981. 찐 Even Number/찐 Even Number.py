import sys
input = sys.stdin.readline

t = int(input().strip())
mod = 10**9+7
for _ in range(t):
    n = int(input().strip())
    if n == 1:
        print(5)
    else:
        print(pow(5,n-1,mod) * 4 % mod)