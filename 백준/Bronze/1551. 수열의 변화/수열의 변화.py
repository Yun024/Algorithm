import sys
input = sys.stdin.readline

n,k = map(int,input().split())
nums = list(map(int,input().split(',')))
for _ in range(k):
    temp = [0]*(n)
    for i in range(1,n):
        temp[i] = nums[i] - nums[i-1]
    nums = temp
print(','.join([str(i) for i in nums[k-n:]]))