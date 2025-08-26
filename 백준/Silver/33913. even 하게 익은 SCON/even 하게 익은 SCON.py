import sys
input = sys.stdin.readline

n = int(input().strip())
mod = 1000000007
ans = ((24+2)**n + (24-2)**n)//2
print(ans%mod)