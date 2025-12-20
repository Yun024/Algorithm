import sys, heapq
input =  sys.stdin.readline

n,m,k = map(int,input().split())
nums = list(map(int,input().split()))
heap = [0]*m

for num in nums:
    temp = heapq.heappop(heap)
    temp += num
    heapq.heappush(heap,temp)

if min(heap) <= k:
    print("WAIT")
else:
    print("GO")