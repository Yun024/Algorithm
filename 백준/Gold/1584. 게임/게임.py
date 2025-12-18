import sys
from collections import deque
input = sys.stdin.readline

def check_rect(diff,x1,y1,x2,y2):
    if x1 > x2: x1,x2 = x2,x1
    if y1 > y2: y1,y2 = y2,y1

    diff[x1][y1] += 1
    diff[x2+1][y1] -= 1
    diff[x1][y2+1] -= 1
    diff[x2+1][y2+1] += 1

def build_grid(diff,size):

    for x in range(size):
        for y in range(size):
            a = diff[x-1][y] if x > 0 else 0 
            b = diff[x][y-1] if y > 0 else 0
            c = diff[x-1][y-1] if x > 0 and y > 0 else 0
            diff[x][y] += a + b - c

    return diff

def solve():

    max = 500
    size = max+1
    diff = size+1

    danger_diff = [[0]*diff for _ in range(diff)]
    death_diff = [[0]*diff for _ in range(diff)]
    dist = [[float("inf")]*size for _ in range(size)]
    dist[0][0] = 0

    n = int(input().strip())
    for _ in range(n):
        x1,y1,x2,y2 = map(int,input().split())
        check_rect(danger_diff,x1,y1,x2,y2)

    m = int(input().strip())
    for _ in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        check_rect(death_diff,x1,y1,x2,y2)
        
    danger = build_grid(danger_diff,size)
    death = build_grid(death_diff,size)
    q = deque()
    q.append([0,0])
    
    if death[max][max] > 0:
        return -1

    while q:
        x,y = q.popleft()
        hp = dist[x][y]
        if x == max and y == max:
            break

        for dx,dy in [[1,0],[-1,0],[0,1],[0,-1]]:
            
            nx,ny = x+dx, y+dy
            if not(0 <= nx <= 500 and 0 <= ny <= 500): continue
            if death[nx][ny] > 0: continue
            w = 1 if danger[nx][ny] > 0 else 0 
            cost = hp + w

            if dist[nx][ny] > cost:
                dist[nx][ny] = cost
                if not w:
                    q.appendleft([nx,ny])
                else:
                    q.append([nx,ny])
                
    ans = dist[max][max]
    return -1 if ans == float("inf") else ans

print(solve())