import sys, heapq
input = sys.stdin.readline

m,n = map(int,input().split())
graph = [list(map(int,input().strip())) for _ in range(n)]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
dist = [[float("inf")]*m for _ in range(n)]
dist[0][0] = 0

heap = [[0,0,0]]
while heap:
    weight,x,y = heapq.heappop(heap)
    if dist[x][y] < weight:
        continue
    if x == n-1 and y == m-1:
        print(weight)
        break

    for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m:
            cost =(weight+1 if graph[nx][ny] else weight)
            if dist[nx][ny] > cost:
                dist[nx][ny] = cost
                heapq.heappush(heap,[cost,nx,ny])