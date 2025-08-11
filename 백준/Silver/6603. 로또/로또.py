from itertools import combinations
import sys
input = sys.stdin.readline

while 1:
    t  = list(map(int,input().split()))
    if not t[0]:
        break
    k,s = t[0],t[1:]
    for i in combinations(s,6):
        print(*i)
    print()