def solution(my_string, n):
    answer = list()
    for i in my_string:
        answer.append(i*n)
    return ''.join(answer)