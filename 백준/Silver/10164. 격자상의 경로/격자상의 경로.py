from collections import deque
import sys
input = sys.stdin.readline

def solution(row,col):
    
    matrix = [[0]*col for _ in range(row)]
    matrix[0][0] = 1
    directions = [[0,1],[1,0]]
    
    for x in range(row):
        for y in range(col):
            for dx,dy in directions:
                nx,ny = x+dx,y+dy
                if 0 <= nx < row and 0 <= ny < col:
                    if not matrix[nx][ny]:
                        matrix[nx][ny] = matrix[x][y]
                    else:
                        matrix[nx][ny] += matrix[x][y]

    return matrix[-1][-1]

n,m,k = map(int,input().split())
if not k:
    print(solution(n,m))
else:
    print(solution((k-1)//m+1,(k-1)%m+1) * solution(n - (k-1)//m , m - (k-1)%m))


