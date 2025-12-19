import sys, heapq
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    s,e,w = map(int,input().split())
    graph[s].append([e,w])
start,end = map(int,input().split())

heap = []
dist = [float("inf")] * (n+1)
dist[start] = 0

heapq.heappush(heap,[0,start])

while heap:
    
    cost,node = heapq.heappop(heap)
    if node == end:
       break

    for next in graph[node]:
        next_node,next_cost = next[0], next[1] + cost
        if next_cost < dist[next_node]:
            dist[next_node] = next_cost
            heapq.heappush(heap,[next_cost,next_node])

print(dist[end])