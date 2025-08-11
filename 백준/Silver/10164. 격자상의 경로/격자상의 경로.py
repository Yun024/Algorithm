from collections import deque
import sys
input = sys.stdin.readline


def solution(start,end):

    ans = 0
    directions = [[0,1],[1,0]]
    q = deque()
    q.append(start)
    ex,ey = end

    while q:
        x,y = q.popleft()
        for dx,dy in directions:
            nx,ny = x+dx,y+dy
            if 0 <= nx < ex and 0 <= ny < ey:
                if nx == ex-1 and ny == ey-1:
                    ans +=1
                else:
                    q.append([nx,ny])

    return ans

n,m,k = map(int,input().split())
if not k:
    print(solution([0,0],[n,m]))
else:
    print(solution([0,0],[(k-1)//m + 1 , (k-1)%m+1]) * solution([(k-1)//m,(k-1)%m],[n,m]))