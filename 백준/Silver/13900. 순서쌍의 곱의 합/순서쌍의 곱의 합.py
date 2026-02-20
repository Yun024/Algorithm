import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))
total = sum(nums)
ans = 0

for n in nums:
    total -= n
    ans += n * total
print(ans)
    