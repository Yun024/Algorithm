import itertools
def solution(numbers):
    return sorted(list(set(map(lambda x: sum(x),itertools.combinations(numbers,2)))))
                
    