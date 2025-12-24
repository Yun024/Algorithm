import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

left,right = 1,min(nums)*m
ans = 0

while left <= right:
    mid = (left+right)//2
    temp = sum([mid//i for i in nums])

    if temp >= m:
        ans = mid
        right = mid-1
    else:
        left = mid+1
print(ans)