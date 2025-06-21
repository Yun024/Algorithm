import sys
from collections import deque
input = sys.stdin.readline

def bfs(n,m):
    
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    visited = [[0]*m for _ in range(n)]
    status = [[0]*m for _ in range(n)]
    matrix = [input().strip() for _ in range(n)]
    
    q = deque()
    q.append((0,0))
    visited[0][0] = 1

    while q:
        ans = visited[n-1][m-1]
        if ans:
            return ans
        
        x,y = q.popleft()
        s = status[x][y]

        for dx,dy in direction:
            nx,ny = x+dx,y+dy
            if 0 <= nx < n and 0 <= ny < m :
                if not visited[nx][ny]:
                    if matrix[nx][ny] == '1' and not s:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                        status[nx][ny] = 1
                    elif matrix[nx][ny] == '0':
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                        status[nx][ny] = s
                else:
                    if not s and status[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
                        if matrix[nx][ny] == '1':
                            status[nx][ny] = 1
                        else:
                            status[nx][ny] = s
    return -1
    
n,m = map(int,input().split())
print(bfs(n,m))