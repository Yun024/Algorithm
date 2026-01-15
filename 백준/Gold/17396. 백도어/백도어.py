import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())
vision = list(map(int,input().split()))

graph = [[] for _ in range(n)]
for _ in range(m):
    start,end,weight = map(int,input().split())
    graph[start].append([weight,end])
    graph[end].append([weight,start])


dist = [float("inf") for _ in range(n)]
dist[0] = 0
heap = []
heapq.heappush(heap,[0,0])

while heap:
    
    weight,node = heapq.heappop(heap)
    if dist[node] < weight:
        continue

    for next_weight,next_node in graph[node]:
        cost = weight + next_weight
        if cost < dist[next_node] and (not vision[next_node] or next_node == n-1):
            dist[next_node] = cost
            heapq.heappush(heap,[cost,next_node])

print(-1 if dist[-1] == float("inf") else dist[-1])