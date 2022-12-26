def solution(rsp):
    answer = list()
    for i in rsp:
        if i == "2":
            answer.append("0") 
        elif i == "5": 
            answer.append("2")
        else :
            answer.append("5")
    return ''.join(answer)