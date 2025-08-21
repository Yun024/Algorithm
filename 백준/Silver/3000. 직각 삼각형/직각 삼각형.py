import sys
from collections import defaultdict
input = sys.stdin.readline
n = int(input().strip())

dic_x = defaultdict(int)
dic_y = defaultdict(int)
xy = []
for _ in range(n):
    x,y = map(int,input().split())
    xy.append([x,y])
    dic_x[f"{x}x"] += 1
    dic_y[f"{y}y"] += 1

ans = 0
for x,y in xy:
    ans += (dic_x[f"{x}x"]-1) * (dic_y[f"{y}y"]-1)

print(ans)
