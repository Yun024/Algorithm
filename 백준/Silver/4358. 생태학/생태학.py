import sys
from collections import Counter

tree = sys.stdin.read().strip().split("\n")
res = Counter(tree)
length = len(tree)

ans = sorted(res.most_common(),key=lambda x: x[0])
for k,v in ans:
    print(f"{k} {v/length*100:.4f}")