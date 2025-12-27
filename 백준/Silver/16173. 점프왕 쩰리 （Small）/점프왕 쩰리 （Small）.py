import sys
from collections import deque
input = sys.stdin.readline

n = int(input().strip())
matrix = [list(map(int,input().split())) for _ in range(n)]

q = deque([(0,0)])
ans = 0
while q:
    x,y = q.pop()
    temp = matrix[x][y]
    if not temp:
        continue
    if temp == -1:
        ans = 1
        break
    if 0 <= x+temp < n:
        q.appendleft((x+temp,y))
    if 0 <= y+temp < n:
        q.appendleft((x,y+temp))

print("HaruHaru" if ans else "Hing")