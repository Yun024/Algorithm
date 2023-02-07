def solution(X, Y):
    answer = ""
    for i in range(0,10):
        answer += str(i) * min(X.count(str(i)),Y.count(str(i)))
    answer = ''.join(sorted(answer,reverse=True))
    if len(answer)==0:
        return "-1"
    elif len(answer.replace("0",""))==0:
        return "0"
    else:
        return answer
    
    # answer = ""
    # for i in X:
    #     if i in Y:
    #         answer += i
    #         Y = Y.replace(i,"",1)
    # final = ''.join(sorted(answer,reverse=True))
    # if len(final)==0:
    #     return "-1"
    # elif len(final.replace("0",""))==0:
    #     return "0"
    # else:
    #     return final