def same_block(m,n,board):
    delete = []
    matrix = [(1,0),(0,1),(1,1)]
    for y in range(m-1):
        for x in range(n-1):
            if board[y][x] != 0 and all(i==board[y][x] for i in [board[y+j][x+i] for j,i in matrix]):
                delete.append((y,x))                     
    loc = set()
    for d in delete:
        loc.add((d))
        for j,i in matrix:
            loc.add((d[0]+j,d[1]+i))
            
    return loc

def change_block(m,n,board,loc):
    for y,x in list(loc):
        board[y][x] = 0
    
    for y in range(m-1,0,-1):
        for x in range(n):
            if not board[y][x]:
                c = 1
                while y-c >= 0:
                    if board[y-c][x]:
                        board[y][x],board[y-c][x] = board[y-c][x],board[y][x]
                        break
                    c +=1
    return board

def solution(m, n, board, ans=0):
    board = [[j for j in i]for i in board]
    loc = [0]
    
    while loc:
        loc = same_block(m,n,board)
        board = change_block(m,n,board,loc)
        ans += len(loc)
    
    return ans