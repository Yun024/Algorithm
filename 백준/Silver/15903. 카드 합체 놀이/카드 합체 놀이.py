import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
nums = list(map(int,input().split()))

heapq.heapify(nums)

for _ in range(m):
    temp = sum([heapq.heappop(nums) for _ in range(2)])
    for _ in range(2):
        heapq.heappush(nums,temp)

print(sum(nums))