import sys
from collections import Counter
input = sys.stdin.readline


n = int(input().strip())
dic = Counter()
for _ in range(n):
    temp = input().split()[2:]
    dic.update(temp)

res = dic.most_common()
if len(res) > 1 and res[0][1] == res[1][1]:
    print(-1)
else:
    print(res[0][0])