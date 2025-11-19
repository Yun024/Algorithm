import sys
from collections import Counter
input = sys.stdin.readline

t = int(input().strip())
res = []
for _ in range(t):
    res.append(input().strip()[0])

ans = Counter(res).most_common()
final = []
for alphabet,num in ans:
    if num >= 5:
        final.append(alphabet)

print(''.join(sorted(final)) if final else 'PREDAJA')