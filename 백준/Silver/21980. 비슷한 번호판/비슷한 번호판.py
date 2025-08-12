import sys, math
from collections import defaultdict
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):

    n,k = map(int,input().split())
    strings = input().split()

    temp = [[] for _ in range(k+1)]
    for s in strings:
        upper_cnt = 0
        for j in s:
            if j.isupper():
                upper_cnt += 1
        temp[upper_cnt].append(s)
    
    dic = defaultdict(int)
    for num in range(k+1):
        for tmp in temp[num]:
            name = str(num) + ''.join(sorted(tmp.lower()))
            dic[name] += 1
    
    ans = 0
    for v in dic.values():
        ans += math.comb(v,2)
    print(ans)