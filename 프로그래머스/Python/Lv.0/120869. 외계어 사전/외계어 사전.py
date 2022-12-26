import itertools
def solution(spell, dic):
    answer = [''.join(i) for i in list(itertools.permutations(spell,len(spell)))]
    return 1 if 1 in [1 if i in answer else 2 for i in dic] else 2