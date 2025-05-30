import sys
nums = list(map(lambda x: int(x), sys.stdin.read().strip().split()))[1:]

import heapq

heap = []
for num in nums:
    if num == 0:
        if heap:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap,num)
