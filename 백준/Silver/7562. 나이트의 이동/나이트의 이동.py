import sys
from collections import deque
input = sys.stdin.readline

def bfs():

    ln = int(input().strip())
    x,y = map(int,input().split())
    gx,gy = map(int,input().split())

    direction = [(-1,-2),(-2,-1),(1,-2),(2,-1),(-1,2),(-2,1),(1,2),(2,1)]
    visited = [[0]*ln for _ in range(ln)]
    visited[x][y] = 1
    q = deque()
    q.append((x,y,0))
    
    while q:
        x,y,num = q.popleft()
        if (x,y) == (gx,gy):
            return num
        
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if 0 <= nx < ln and 0 <= ny < ln and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny,num+1))


n = int(input().strip())
for _ in range(n):
    print(bfs())