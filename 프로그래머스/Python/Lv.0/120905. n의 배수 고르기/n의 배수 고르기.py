def solution(n, numlist):
    answer = list()
    for i in numlist :
        if i % n == 0:
            answer.append(i)
    return answer