def solution(num):
    answer = [num]
    while num != 1:
        if num % 2 == 0:
            num = num / 2
            answer.append(num)
        else :
            num = num * 3 +1 
            answer.append(num)
    return -1 if len(answer)-1>500 else len(answer)-1