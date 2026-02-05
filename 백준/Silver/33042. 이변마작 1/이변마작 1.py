import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().strip())
dic = defaultdict(int)
tiles = input().split()
for i,t in enumerate(tiles):
    dic[t] += 1
    if dic[t] == 5:
        print(i+1)
        break
else:
    print(0)