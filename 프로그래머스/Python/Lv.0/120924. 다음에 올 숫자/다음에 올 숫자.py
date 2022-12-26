def solution(common):
    
    if (common[2] - common[1]) == (common[1] - common[0]):
        answer = common[len(common)-1] + (common[1] - common[0])
    else :
        answer = common[len(common)-1] * (common[1]/common[0])
    
    return answer
