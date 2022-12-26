def solution(num, k):
    answer = 1
    for i in str(num):
        if i == str(k):
            break
        else: answer += 1
    return -1 if answer > len(str(num)) else answer