import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))
ans = [-1]
for i in range(1,n):
    if nums[-i] > nums[-i-1]:
        temp = nums[-i-1]
        nums[-i-1] = min([j for j in nums[-i:] if j > temp])
        second_part = sorted([temp if j == nums[-i-1] else j for j in nums[-i:]])
        ans = nums[:-i] + second_part
        break
print(*ans)