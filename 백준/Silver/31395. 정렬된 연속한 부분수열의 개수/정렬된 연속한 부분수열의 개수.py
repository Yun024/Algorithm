import sys, math
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))

ans = 0
temp = 1
for i in range(1,n):
    ans += temp
    if nums[i] > nums[i-1]:
        temp += 1
    else:
        temp =1
ans += temp
print(ans)