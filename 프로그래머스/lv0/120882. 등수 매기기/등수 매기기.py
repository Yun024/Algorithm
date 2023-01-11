import numpy as np
def solution(score):
    score_sort = list(map(lambda x: np.mean(x),score))
    answer = sorted(list(map(lambda x: np.mean(x),score)),reverse=True)
    return [answer.index(i)+1 for i in score_sort]