def solution(k, score):
    return [sorted(score[:i+1])[-k:][0] for i in range(len(score))]
    