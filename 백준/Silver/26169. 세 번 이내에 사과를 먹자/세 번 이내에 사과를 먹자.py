import sys
input = sys.stdin.readline

graph = [list(map(int,input().split())) for _ in range(5)]
r,c = map(int,input().split())
visited =[[0]*5 for _ in range(5)]
visited[r][c] = 1
directions = [(1,0),(-1,0),(0,1),(0,-1)]

def dfs(x,y,move,apple):

    if apple >= 2:
        return 1

    if move == 3:
        return 0
    
    for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if 0 <= nx < 5 and 0 <= ny < 5 and not visited[nx][ny]:
            if graph[nx][ny] == -1:
                continue

            visited[nx][ny] = 1
            next_apple = apple + (1 if graph[nx][ny] == 1 else 0)

            res = dfs(nx,ny,move+1,next_apple)
            visited[nx][ny] = 0

            if res ==1:
                return 1
    return 0

apple = (1 if graph[r][c] == 1 else 0)
if graph[r][c] == -1:
    print(0)
else:
    print(dfs(r,c,0,apple))