from collections import defaultdict, deque
def solution(storage,requests):
    
    n,m = len(storage), len(storage[0])
    storage = [[0]*(m+2)] + [[0] + [j for j in i] + [0] for i in storage] + [[0]*(m+2)]
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    dic = defaultdict(list)
    for i in range(n+2):
        for j in range(m+2):
            dic[storage[i][j]].append([i,j])
    
    for request in requests:
        if len(request) == 2:
            for x,y in dic[request[0]]:
                storage[x][y] = 0
            dic[request[0]] = [[0,0]]
        else:
            queue = deque()
            queue.append((0,0))
            visited = [[0]*(m+2) for _ in range(n+2)]
            visited[0][0] = 1   
            
            while queue:
                x,y = queue.popleft()
                for dx,dy in directions:
                    nx,ny = x+dx, y+dy
                    if( 
                        0 <= nx < n+2 and 
                        0 <= ny < m+2 and
                        not visited[nx][ny] 
                    ):
                        if storage[nx][ny] == request:
                            visited[nx][ny] = 1
                            storage[nx][ny] = 0
                        elif not storage[nx][ny]:
                            queue.append([nx,ny])
                            visited[nx][ny] = 1
    return sum([len([j for j in i if j]) for i in storage])