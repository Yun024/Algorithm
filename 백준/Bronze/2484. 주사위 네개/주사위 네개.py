import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
ans = []
for _ in range(n):
    nums = sorted(list(map(int,input().split())))
    num_cnt  = Counter(nums).most_common()
    if len(num_cnt) == 1:
        ans.append(num_cnt[0][0]*5000+50000)
    elif len(num_cnt) == 2:
        if num_cnt[0][1] == 3:
            ans.append(num_cnt[0][0]*1000+10000)
        else:
            ans.append(num_cnt[0][0]*500+num_cnt[1][0]*500+2000)
    elif len(num_cnt) == 3:
        ans.append(num_cnt[0][0]*100+1000)
    else:
        ans.append(max(nums)*100)
print(max(ans))