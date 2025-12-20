import sys, heapq
input =  sys.stdin.readline

n = int(input().strip())
heap = []
for _ in range(n):
    temp = input().strip()
    if temp == "0":
        if not heap:
            print(-1)
        else:
            print(abs(heapq.heappop(heap)))
    else:
        for t in list(map(int,temp.split()))[1:]:
            heapq.heappush(heap,-t)