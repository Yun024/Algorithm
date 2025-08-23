import sys,math
input = sys.stdin.readline

mod = 998244353
n = int(input().strip())
nums = list(map(int,input().split()))

print(pow(n-2,n,mod))
