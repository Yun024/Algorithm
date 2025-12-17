import sys
import heapq
input = sys.stdin.readline

n,d = map(int,input().split())
graph = {}
dist = [float("inf")]*(d+1)
dist[0] = 0
heap = []
heapq.heappush(heap,(0,0))

for _ in range(n):
    start,end,weight = map(int,input().split())
    if not start < end <= d:
        continue
    if not graph.get(start):
        graph[start] = [[end,weight]]
    else:
        graph[start].append([end,weight])


while heap:
    node,cost = heapq.heappop(heap)
    if dist[node] < cost:
        continue
    else:
        dist[node] = cost
        if graph.get(node):
            for next_node in graph[node]:
                heapq.heappush(heap,(next_node[0],next_node[1]+cost))
        if node+1 <= d:
            heapq.heappush(heap,(node+1,cost+1))

print(dist[d])