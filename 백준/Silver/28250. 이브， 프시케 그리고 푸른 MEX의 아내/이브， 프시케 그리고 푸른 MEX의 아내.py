import sys
from collections import Counter
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))


ans = 0
cnt = Counter(nums)
ans += cnt[0] * cnt[1] * 2
ans += cnt[0] * (cnt[0]-1) // 2
ans += cnt[0] * (len(nums) - cnt[1] - cnt[0])
print(ans)

