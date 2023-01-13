
def solution(board):
    answer = ["O" for i in range(len(board)*len(board))] 
    right = list(range(len(board)*len(board)))[len(board)-1::len(board)]
    left = list(range(len(board)*len(board)))[::len(board)]
    up = list(range(len(board)))
    
    for j,i in enumerate(sum(board,[])):
        if len(board)<3 and 1 in sum(board,[]):
            return 0
        else:
            if i == 1:
                if j in right:
                    try:
                        answer[j] = "X"
                        answer[j-1] = "X"
                        answer[j-len(board)] = "X"
                        answer[j-len(board)-1] = "X"
                        answer[j+len(board)] = "X"
                        answer[j+len(board)-1] = "X"
                    except IndexError:
                        pass
                elif j in left:
                    try:
                        answer[j] = "X"
                        answer[j+1] = "X"
                        answer[j-len(board)] = "X"
                        answer[j-len(board)+1] = "X"
                        answer[j+len(board)] = "X"
                        answer[j+len(board)+1] = "X"
                    except IndexError:
                        pass
                else:
                    try:
                        answer[j] = "X"
                        answer[j-1] = "X"
                        answer[j+1] = "X"
                        answer[j-len(board)] = "X"
                        answer[j-len(board)+1] = "X"
                        answer[j-len(board)-1] = "X"
                        answer[j+len(board)] = "X"
                        answer[j+len(board)+1] = "X"
                        answer[j+len(board)-1] = "X"
                    except IndexError:
                        pass
                if j in up :
                        for i in up:
                            answer[-i] = "O"
                
    return answer.count("O")