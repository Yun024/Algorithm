import sys,heapq
input = sys.stdin.readline

n,m = map(int,input().split())

dist = [float("inf")]*(n+1)
dist[0] = 0

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

s,t = map(int,input().split())

heap = []
heapq.heappush(heap,(0,s))

while heap:
    prefix_cost,node = heapq.heappop(heap)
    for next in graph[node]:
        weight,next_node = next
        next_cost = weight + prefix_cost
        if dist[next_node] > next_cost:
            dist[next_node] = next_cost
            heapq.heappush(heap,(next_cost,next_node))

print(dist[t])