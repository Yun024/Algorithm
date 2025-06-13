import sys
from collections import deque
input = sys.stdin.readline

def bfs(matrix):

    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    visited = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0,0,1))

    while q:
        x,y,cnt = q.popleft()
        if x == n-1 and y == m-1:
            return cnt
        
        for dx,dy in direction:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and int(matrix[nx][ny]) and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx,ny,cnt+1))

n,m = map(int,input().split())
matrix = [input().strip() for _ in range(n)]
print(bfs(matrix))