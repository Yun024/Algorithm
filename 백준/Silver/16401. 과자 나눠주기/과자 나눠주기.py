import sys
input = sys.stdin.readline

m,n = map(int,input().split())
nums = list(map(int,input().split()))

left,right = 1,max(nums)
ans = 0

while left <= right:
    mid = (left+right)//2
    res = [i//mid for i in nums]
    if sum(res) >= m:
        ans = mid
        left = mid+1
    else:
        right = mid-1

print(ans)