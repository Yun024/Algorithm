def solution(board, moves):
    answer = []
    ans = 0
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0 :
                answer.append(board[j][i-1])
                board[j][i-1] = 0
                if len(answer)>1:
                    if answer[-1] == answer[-2]:
                        answer.pop()
                        answer.pop()
                        ans +=2
                break                    
    return ans

    # 최초풀이
    # for i in moves:
    #     for j in range(len(board)):
    #         if j == len(board)-1 and board[j][i-1] == 0:
    #             answer.append(0)
    #         if board[j][i-1] != 0:
    #             if answer[-1] == board[j][i-1] :
    #                 ans += 2
    #                 answer.pop()
    #             else:
    #                 answer.append(board[j][i-1])
    #             board[j][i-1]= 0
    #             break
    # return ans
    


# 00000
# 00103
# 02501
# 42442
# 35131

