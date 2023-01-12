
from itertools import combinations
def minus(x):
    return x[1] - x[0]
def solution(dots):
    comb = list(combinations(dots,2))
    a = list(combinations(dots,2))[:3]
    b = list(combinations(dots,2))[3:][::-1]
    a_grad = [minus(sum(i,[])[1::2])/minus(sum(i,[])[::2]) for i in a]
    b_grad = [minus(sum(i,[])[1::2])/minus(sum(i,[])[::2]) for i in b]
    for i in range(len(a_grad)):
        if a_grad[i] == b_grad[i]:
            return 1
    return 0
    