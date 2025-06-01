import sys, heapq

nums = list(map(int,sys.stdin.read().strip().split("\n")))[1:]
heap = []

for num in nums:
    if not num:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,[abs(num),num])