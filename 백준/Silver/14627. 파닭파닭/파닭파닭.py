import sys
input = sys.stdin.readline

s,c = map(int,input().split())
nums = [int(input().strip()) for i in range(s)]
left,right = 1,max(nums)
ans = 0

while left <= right:
    mid = (left+right)//2
    temp = sum([i//mid for i in nums])
    if temp >= c:
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(sum(nums) - c*ans)