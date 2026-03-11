import sys
input = sys.stdin.readline

n,m = map(int,input().split())
scores = list(map(int,input().split()))

print("OUT" if sum(scores) - n < m else "DIMI")