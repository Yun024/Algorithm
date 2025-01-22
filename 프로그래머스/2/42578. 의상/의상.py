import math
def solution(clothes):
    dic = {}
    for j,i in clothes:
        if dic.get(i):
            dic[i].append(j)
        else:
            dic[i] = [j]
            dic[i].append("")
    return math.prod([len(i) for i in dic.values()]) -1