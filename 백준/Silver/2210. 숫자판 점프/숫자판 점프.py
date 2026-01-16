import sys
board = [list(map(int,sys.stdin.readline().split())) for _ in range(5)]

def dfs(start,res,cnt):

    x,y = start
    res += str(board[x][y])

    if cnt+1 == 6:     
        ans.add(res)
        return

    for dx,dy in directions:
        nx,ny = x+dx, y+dy
        if 0 <= nx < 5 and 0<= ny < 5:
            cnt += 1
            dfs([nx,ny],res,cnt)
            cnt -= 1
    
    


start = [0,0]
directions = [(1,0),(-1,0),(0,1),(0,-1)]
ans = set()

for i in range(5):
    for j in range(5):
        dfs([i,j],"",0)

print(len(ans))