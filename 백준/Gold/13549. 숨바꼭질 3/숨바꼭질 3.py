import sys,heapq
input = sys.stdin.readline
n,k = map(int,input().split())

def solve(n,k):

    if n >= k:
        return n-k
    
    dist = [float("inf")]*(k*2)
    dist[n] = 0

    heap = []
    heapq.heappush(heap,(0,n))

    while heap:
        weight, now = heapq.heappop(heap)
        if dist[now] < weight:
            continue

        if now == k:    
            return weight
        
        for nw,nm in [(1,-1),(1,1),(0,2)]:
            if not nw:
                cost = weight
                next = now * nm
            else:
                cost = weight + nw
                next = now + nm

            if 0 <= next < (k*2):
                if dist[next] > cost:
                    dist[next] = cost
                    heapq.heappush(heap,(cost,next))
    return dist[k]
print(solve(n,k))