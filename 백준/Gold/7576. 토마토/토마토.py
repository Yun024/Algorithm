import sys
from collections import deque
input = sys.stdin.readline

def find_start(box):

    start = []
    for x in range(n):
        for y in range(m):
            if box[x][y] == '1':
                start.append([x,y])
    return start

def bfs(start):

    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque()
    for s in start:
        q.append(s+[1])
    
    while q:
        x,y,cnt = q.popleft()
        
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == '0':
                box[nx][ny] = '1'
                q.append((nx,ny,cnt+1))

    for x in range(n):
        for y in range(m):
            if box[x][y] == '0':
                return -1
    return cnt -1

m,n = map(int,input().split())
box = [input().split() for _ in range(n)]
start = find_start(box)
print(bfs(start))
