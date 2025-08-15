import sys, math
from collections import Counter
input = sys.stdin.readline

name = input().strip()
n = int(input().strip())
strings = [c[0] for _ in range(n) for c in [input().strip()] if c[0] in name]

ans = 1
for key,value in Counter(name).items():
    ans *= math.comb(strings.count(key),value)
print(ans) 