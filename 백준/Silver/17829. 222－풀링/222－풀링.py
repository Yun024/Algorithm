import sys
input = sys.stdin.readline

n = int(input().strip())
board = [list(map(int,input().split())) for _ in range(n)]

while n != 1:
    res = []
    for i in range(0,n,2):
        temp = []
        for j in range(0,n,2):
            temp.append(sorted([board[i][j],board[i+1][j],board[i][j+1],board[i+1][j+1]])[-2])
        res.append(temp)
    board = res
    n //= 2

print(board[0][0])