import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))

ans,temp = 0,1
for i in range(1,max(nums)+1):
    temp *= nums.count(i)
    ans += temp
    if not temp:
        break
print(ans)
    