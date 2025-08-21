import sys, math
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
right = [[] for _ in range(n+1)]
for _ in range(m):
    l,r = map(int,input().split())
    right[r].append(l)

right = [i for i in right if len(i) >= 2]
ans = 0

for r1,r2 in list(combinations(right,2)):
    ans += math.comb(len(set(r1)&set(r2)),2)

print(ans)