import sys, heapq
input = sys.stdin.readline

n,m,a,b,c = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start,end,cost = map(int,input().split())
    graph[start].append([cost,end])
    graph[end].append([cost,start])


dist = [[float("inf"),float("inf")] for _ in range(n+1)]
dist[a] = [0,0]
heap = [[0,0,a]]

while heap:
    weight,stress,node = heapq.heappop(heap)
    for nweight,nnode in graph[node]:
        new_stress = max(nweight,stress)
        new_weight = weight + nweight

        next_weight,next_stress = dist[nnode]
        if new_weight <= c and (new_weight < next_weight or new_stress < next_stress):
            dist[nnode][0] = min(new_weight,next_weight)
            dist[nnode][1] = min(new_stress,next_stress)
            heapq.heappush(heap,[new_weight,new_stress,nnode])

ans = dist[b][1]
print(ans if ans != float("inf") else -1)