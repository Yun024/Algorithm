import sys

nums = list(map(lambda x: sum(int(i) for i in x),sys.stdin.readline().split()))
print(nums[0]*nums[1])

