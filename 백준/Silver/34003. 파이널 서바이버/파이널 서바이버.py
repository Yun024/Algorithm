import sys,math
input = sys.stdin.readline

matrix = [input().strip() for _ in range(8)]
ans_mat = [[0]*9 for _ in range(9)]
directions = [[0,1],[0,0],[1,0],[1,1]]
cnt = 0

for x in range(8):
    for y in range(8):
        if matrix[x][y] == 'O':
            cnt += 1
            for dx,dy in directions:
                nx,ny = x+dx, y+dy
                ans_mat[nx][ny] += 1

temp = 0 
for x in range(1,8):
    for y in range(1,8):
        if ans_mat[x][y] > temp:
            ans1 = [x,y]
            temp = ans_mat[x][y]

ans2 = math.comb((cnt-temp),4) / math.comb(cnt,4)
print(*ans1)
print(1 - ans2)