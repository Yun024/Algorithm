import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(m)]
directions = [(1,0),(0,1)]

visited = [[0]*n for _ in range(m)]
visited[0][0] = 1

def dfs(x,y):

    if x == m-1 and y == n-1:
        return 1
    
    for dx,dy in directions:
        nx,ny = x+dx,y+dy
        if 0 <= nx < m and 0 <= ny < n and graph[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            res = dfs(nx,ny)
            if res:
                return 1
    return 0
            
print("Yes" if dfs(0,0) else "No")