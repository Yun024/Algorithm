from collections import deque

def find_start(maps):
    for x,i in enumerate(maps):
        for y,j in enumerate(i):
            if j == "S":
                return x,y
            
def bfs(start, goal, maps):
    
    direction = [(1,0),(0,1),(-1,0),(0,-1)]
    x,y = start
    visited = set()
    visited.add((x,y))
    
    queue = deque()
    queue.append((x,y,0))
    
    while queue:
        x,y,cnt = queue.popleft()
        
        for dx,dy in direction:
            nx, ny = x + dx, y+dy
            if (nx,ny) not in visited and 0 <= nx < len(maps) \
            and 0 <= ny < len(maps[0]) and maps[nx][ny] != "X":
                if maps[nx][ny] == goal:
                    return nx,ny,cnt+1
                else:
                    visited.add((nx,ny))
                    queue.append((nx,ny,cnt+1))
    return -1 

                        
def solution(maps):
    
    start = find_start(maps)
    L_result = bfs(start,"L",maps)
    if L_result == -1:
        return -1
    lx,ly,cnt = L_result
    
    E_result = bfs((lx,ly),"E",maps)
    if E_result == -1:
        return -1
    return cnt + E_result[2]
    
    
    