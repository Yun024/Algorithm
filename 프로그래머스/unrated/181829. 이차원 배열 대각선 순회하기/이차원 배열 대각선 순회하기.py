
def solution(board, k):
    answer = []
    for j,i in enumerate(board):
        for c,u in enumerate(i):
            if j+c <= k :
                answer.append(board[j][c])
    return sum(answer)
                
    