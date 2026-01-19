from collections import deque
import numpy as np
def solution(land):
    
    row,col = len(land), len(land[0])
    visited = [[0] * col for _ in range(row)]
    prefix_sum = [[0] * col for _ in range(row)]
    directions = [[0,1],[0,-1],[1,0],[-1,0]]
    dic,num = {}, 1
    
    for r in range(row):
        for c in range(col):
            if visited[r][c]:
                continue
            visited[r][c] = 1
            if land[r][c] == 1:
                oil = 1
                res = [[r,c]]
                q = deque([[r,c]])
                
                while q:
                    x,y = q.popleft()
                    for dx,dy in directions:
                        nx,ny = x+dx,y+dy
                        if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and land[nx][ny]:
                            oil += 1
                            visited[nx][ny] = 1
                            q.append([nx,ny])
                            res.append([nx,ny])
                
                dic[num] = oil
                for x,y in res:
                    prefix_sum[x][y] = num
                num += 1
    
    ans = 0
    for c in range(col):
        visit = []
        sum_row = 0
        for r in range(row):
            if prefix_sum[r][c] and prefix_sum[r][c] not in visit:
                visit.append(prefix_sum[r][c])
                sum_row += dic[prefix_sum[r][c]]
        ans = max(ans,sum_row)
                
                
    return ans