def solution(board):
    
    x_ln = len(board)
    y_ln = len(board[0])
    if x_ln == 1 and y_ln == 1:
        return 1
    directions = [[-1,0],[-1,-1],[0,-1]]
    square = [[board[x][y] for y in range(y_ln)] for x in range(x_ln)]
    ans = 0
    
    for x in range(1,x_ln):
        for y in range(1,y_ln):
            if not board[x][y]:
                square[x][y] = 0
            else:
                temp = [square[x+dx][y+dy] for dx,dy in directions]
                square[x][y] = min(temp) + 1
                ans = max(ans,square[x][y])
    return ans**2
                
    
        