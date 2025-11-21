import sys

nums = sum(map(lambda x: int(x[::-1]),sys.stdin.readline().split()))
print(int(str(nums)[::-1]))