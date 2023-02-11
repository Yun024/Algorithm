def solution(sizes):
    answer = [sorted(i,reverse=True) for i in sizes]
    return max(sum(answer,[])[::2]) * max(sum(answer,[])[1::2])