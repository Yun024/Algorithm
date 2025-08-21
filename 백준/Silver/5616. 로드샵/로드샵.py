import sys, math

n,m,r = map(int,sys.stdin.readline().split())

def solution(n,m,r):
    
    if n*m > r:
        return 0
    if not m:
        return math.comb(n+r-1,r)
    r -= n*m
    return math.comb(n+r-1,r)

print(solution(n,m,r))