def solution(s):
    zz = list(s)
    answer = []
    for i in s:
        if zz.count(i) == 1:
            answer.append(i)
    return ''.join(sorted(answer))