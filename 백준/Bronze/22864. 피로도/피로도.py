import sys

nums = list(map(int,sys.stdin.readline().split()))
ans,time,stress = 0,0,0

while time < 24:
    if stress + nums[0] <= nums[3]:
        stress += nums[0]
        ans += nums[1]
    else:
        stress = max(stress-nums[2],0)
    time += 1

print(ans)