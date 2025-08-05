import sys
from collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    clothes = defaultdict(int)
    for _ in range(n):
        _,tp = input().split()
        clothes[tp] += 1
    ans = 1
    for i in clothes.values():
        ans *= i+1
    print(ans-1)

    