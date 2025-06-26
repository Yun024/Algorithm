import sys
sys.setrecursionlimit(10**6)

def solution(maps):
    
    def dfs(start):
        x,y = start
        cnt = int(maps[x][y])
        for dx,dy in directions:
            nx,ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and maps[nx][ny] != "X":
                visited[nx][ny] = 1
                cnt += int(dfs((nx,ny)))
                print(cnt)
        return cnt
    
    n,m = len(maps), len(maps[0])
    visited = [[0]*m for _ in range(n)]
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    ans = []
    for row in range(n):
        for col in range(m):
            if maps[row][col] != "X" and not visited[row][col]:
                visited[row][col] = 1
                ans.append(dfs((row,col)))
    return sorted(ans) if ans else [-1]