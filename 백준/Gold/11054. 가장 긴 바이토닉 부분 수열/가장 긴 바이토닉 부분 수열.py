import sys

def bitonic(n,nums):

    LIS = [1] * n
    LDS = [1] * n

    for i in range(1,n):
        for j in range(i):
            if nums[i] > nums[j]:
                LIS[i] = max(LIS[i],LIS[j]+1)

    for i in range(n-1,-1,-1):
        for j in range(n-1,i,-1):
            if nums[i] > nums[j]:
                LDS[i] = max(LDS[i],LDS[j]+1)

    
    return max([i+j for j,i in zip(LDS,LIS)]) - 1

input = sys.stdin.readline
n = int(input().strip())
nums = list(map(int,input().split()))

print(bitonic(n,nums))