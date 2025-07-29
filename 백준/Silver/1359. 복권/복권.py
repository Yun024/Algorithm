import sys,math
from itertools import combinations
input = sys.stdin.readline

n,m,k = map(int,input().split())
nums = [i for i in range(n)]
down = math.comb(n,m) * math.comb(n,m)

up = 0
for i in list(combinations(nums,m)):
    for j in list(combinations(nums,m)):
        temp = 0
        for t in j:
            if t in i:
                temp +=1
        if temp >= k:
            up +=1

print(up/down)