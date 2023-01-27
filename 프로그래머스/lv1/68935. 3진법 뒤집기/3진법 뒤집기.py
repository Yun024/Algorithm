def solution(n):
    answer =[]
    while n>2:
        answer.append(n%3)
        n = n//3
    answer.append(n*3//3)
    return int(''.join(map(str,answer)),3)
    