import heapq
def solution(N,road,K):
    
    graph = [[] for _ in range(N+1)]
    for start,end,weight in road:
        graph[start].append((weight,end))
        graph[end].append((weight,start))
    
    INF = 10**6
    dist = [INF]*(N+1)
    dist[0] = 0
    dist[1] = 0
    
    heap = []
    heapq.heappush(heap,(0,1))
    
    while heap:
        weight,node = heapq.heappop(heap)
        
        if dist[node] < weight:
            continue
            
        for nxt in graph[node]:
            next_weight, next_node = nxt
            cost = weight + next_weight
            
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(heap,(cost,next_node))
               
    return len([i for i in dist[1:] if i <= K])
    