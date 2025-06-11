import sys
sys.setrecursionlimit(2510)
input = sys.stdin.readline

def dfs(node):
    
    x,y = node
    visited[x][y] = 1
    dir = [(0,1),(1,0),(-1,0),(0,-1)]

    for dx,dy in dir:
        nx,ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] and not visited[nx][ny]:
            dfs((nx,ny))
    return 1

n = int(input().strip())
for _ in range(n):
    
    m,n,k = map(int,input().split())
    
    visited = [[0]*m for _ in range(n)]
    matrix = [[0]*m for _ in range(n)]
    ans = 0

    for _ in range(k):
        v,u = map(int,input().split())
        matrix[u][v] += 1


    for x in range(n):
        for y in range(m): 
            if matrix[x][y] and not visited[x][y]:
                ans += dfs((x,y))
            
    print(ans)

