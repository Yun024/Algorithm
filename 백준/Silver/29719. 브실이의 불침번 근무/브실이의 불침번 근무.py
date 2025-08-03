import sys, math
n,m = map(int,sys.stdin.readline().split())

mod = 1000000007
ans = pow(m,n,mod) - pow(m-1,n,mod)
print(ans%mod)