import sys,heapq
input = sys.stdin.readline

n = int(input().strip())
heap = []
for _ in range(n):
    for i in list(map(int,input().split())):
        if len(heap) == n+1:
            heapq.heappop(heap)
        heapq.heappush(heap,i)

if len(heap) == n+1:
    heapq.heappop(heap)
print(heap[0])