import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x,y):

    directions = [[1,0],[-1,0],[0,1],[0,-1],[1,-1],[1,1],[-1,1],[-1,-1]]
    for dx,dy in directions:
        nx,ny = x+dx,y+dy
        if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and land[nx][ny]:
            visited[nx][ny] = 1
            dfs(nx,ny)

while 1:
    w,h = map(int,input().split())
    if w == h == 0:
        break
    elif w == h == 1:
        print(int(input().strip()))
        continue
    
    land = [list(map(int,input().split())) for i in range(h)]
    visited = [[0]*w for _ in range(h)]
    ans = 0
    for x in range(h):
        for y in range(w):
            if land[x][y] and not visited[x][y]:
                visited[x][y] = 1
                ans += 1
                dfs(x,y)
    
    print(ans)
