import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))
ans = 0
total = sum(nums)

for num in nums:
    total -= num
    ans += num * total

print(ans)