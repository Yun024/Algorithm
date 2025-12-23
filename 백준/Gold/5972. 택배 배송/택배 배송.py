import sys, heapq
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
heap = []
heapq.heappush(heap,[0,1])
dist = [float("inf")]*(n+1)
dist[0],dist[1] = 0,0

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
     
while heap:
    weight,node = heapq.heappop(heap)
    if node == n:
        break
    
    for next in graph[node]:
        next_node,next_weight = next
        cost = weight + next_weight
        if dist[next_node] > cost:
            dist[next_node] = cost
            heapq.heappush(heap,[cost,next_node])    
print(dist[-1])
    