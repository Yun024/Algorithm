def solution(order):
    answer= 0
    for i in str(order):
        if int(i) == 3:
            answer += 1
        elif int(i) == 6:
            answer += 1
        elif int(i) == 9:
            answer +=1
        else:
            continue
    return answer