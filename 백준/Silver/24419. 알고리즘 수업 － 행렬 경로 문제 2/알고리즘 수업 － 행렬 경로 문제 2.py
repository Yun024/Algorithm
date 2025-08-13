import sys,math
input = sys.stdin.readline

n = int(input().strip())
matrix = [list(map(int,input().split())) for i in range(n)]
mod = 1000000007
print(math.comb(n*2,n)%mod,n**2%mod)