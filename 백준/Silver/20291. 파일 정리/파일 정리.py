import sys
from collections import defaultdict

input = sys.stdin.readline
t = int(input().strip())
dic = defaultdict(int)
for _ in range(t):
    _,name = input().strip().split(".")
    dic[name] += 1
for i in sorted(dic.items()):
    print(*i)