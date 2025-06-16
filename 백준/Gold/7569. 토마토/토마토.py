import sys
from collections import deque
input = sys.stdin.readline

def bfs(m,n,h):

    box = []
    for _ in range(h):
        floor = []
        for _ in range(n):
            floor.append(list(map(int,input().split())))
        box.append(floor)

    q = deque()
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if box[x][y][z] == 1:
                    q.append((x,y,z))

    direction = [(0,-1,0),(0,1,0),(0,0,-1),(0,0,1),(1,0,0),(-1,0,0)]
    while q:
        x,y,z = q.popleft()    

        for dx,dy,dz in direction:
            nx,ny,nz = x+dx, y+dy, z+dz
            if 0 <= nx < h and 0 <= ny < n and 0 <= nz < m and not box[nx][ny][nz]:
                box[nx][ny][nz] = box[x][y][z] +1
                q.append((nx,ny,nz))

    ans = 0
    for x in range(h):
        for y in range(n):
            for z in range(m):
                if not box[x][y][z]:
                    return -1
                ans = max(ans,box[x][y][z])

    return ans-1

m,n,h = map(int,input().split())
print(bfs(m,n,h))