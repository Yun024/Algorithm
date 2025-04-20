import sys

def dp(n,nums):

    if n <= 2:
        return sum(nums)

    org = nums[:]
    step = [0] * (n)
    step[0] = org[0]
    step[1] = step[0] + org[1]
    step[2] = max(step[1],org[0]+org[2],org[1]+org[2])

    for i in range(3,n):
        step[i] = max(step[i-1],org[i]+org[i-1]+step[i-3],org[i]+step[i-2])

    return step[-1]
  
n = int(sys.stdin.readline().strip())
nums = [int(sys.stdin.readline().strip()) for _ in range(n)]
print(dp(n,nums))