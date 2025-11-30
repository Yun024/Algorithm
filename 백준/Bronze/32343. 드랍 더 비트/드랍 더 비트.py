import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input().strip())
a,b = map(int,input().split())


aa = list(('1'*a).zfill(n))
bb = list(('1'*b).zfill(n))
aaa = list(set(permutations(aa,n)))
bbb = set(permutations(bb,n))

ans = 0
for i in aaa:
    for j in bbb:
        ans = max(ans,int(''.join(i),2)^int(''.join(j),2))
print(ans)