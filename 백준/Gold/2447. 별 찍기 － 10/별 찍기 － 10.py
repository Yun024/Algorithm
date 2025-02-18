def draw_star(board, x, y, size):
    pattern = ["***","* *","***"]
    if size == 3:
        for i in range(3):
            for j in range(3):
                board[x+i][y+j] = pattern[i][j]
        return
    
    new_size = size//3
    for i in range(3):
        for j in range(3):
            if i == j == 1:
                continue
            draw_star(board, x+i*new_size, y+j*new_size, new_size)

n = int(input())
board = [[" "] * n for i in range(n)]

draw_star(board, 0, 0, n)

for i in board:
    print(''.join(i))