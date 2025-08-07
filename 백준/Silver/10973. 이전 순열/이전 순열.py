import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))
ans = [-1]

for i in range(1,n):
    if nums[-i] < nums[-i-1]:
        j = nums.index(max([j for j in nums[-i:] if j < nums[-i-1]]))
        nums[-i-1],nums[j] = nums[j],nums[-i-1]
        ans = nums[:-i] + sorted(nums[-i:],reverse=True)
        break
print(*ans)