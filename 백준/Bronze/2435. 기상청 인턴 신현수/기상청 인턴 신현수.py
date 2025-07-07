import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split()))

total = -10000
for i in range(n-k+1):
    total = max(total,sum(nums[i:i+k]))

print(total)