import sys

def dfs(node):
    
    global cnt
    cnt +=1

    x,y = node
    visited[x][y] = 1
    
    direction = [(0,1),(1,0),(-1,0),(0,-1)]
    for dx,dy in direction:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and map[nx][ny] == "1":
            dfs((nx,ny))
            


n = int(sys.stdin.readline().strip())
map = sys.stdin.read().strip().split("\n")
visited = [[0] * n for _ in range(n)]

ans = []
for x in range(n):
    for y in range(n):
        if map[x][y] == "1" and not visited[x][y]:
            cnt = 0
            dfs((x,y))
            ans.append(cnt)

print(len(ans))
for i in sorted(ans):
    print(i)