def solution(d, budget):
    for j,i in enumerate(sorted(d)):
        budget -= i
        if budget < 0:
            return j
        elif budget == 0:
            return j+1
    return len(d)
    