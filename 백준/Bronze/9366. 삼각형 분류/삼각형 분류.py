import sys
input = sys.stdin.readline

t = int(input().strip())
for n in range(t):
    nums = sorted(map(int,input().split()))
    if nums[-1] == nums[0]:
        ans = "equilateral"
    elif nums[-1] >= nums[0] + nums[1]:
        ans = "invalid!"
    elif nums[-1] == nums[1] or nums[0] == nums[1]:
        ans = "isosceles"
    else:
        ans = "scalene"
    print(f"Case #{n+1}: {ans}")