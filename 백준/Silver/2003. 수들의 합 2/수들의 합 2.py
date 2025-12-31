import sys
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

ans = 0
left,right = 0,0
temp = nums[left]

while left <= right:
    if temp <= m:
        if temp == m:
            ans += 1
        if right == n-1:
            break
        right += 1
        temp += nums[right]
    else:
        if left == right:
            if left == n-1:
                break
            right += 1
            temp += nums[right]
        
        temp -= nums[left]
        left += 1

print(ans)