import itertools
def solution(number):
    return len([i for i in list(itertools.combinations(number,3)) if sum(i)==0])