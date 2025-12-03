import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = [int(input().strip()) for _ in range(n)]
left,right = 1,max(nums)
ans = 0

while left <= right:
    mid = (left+right)//2
    temp = sum([i//mid for i in nums])
    if temp >= k:
        ans = mid
        left = mid+1
    else:
        right = mid-1
print(ans)