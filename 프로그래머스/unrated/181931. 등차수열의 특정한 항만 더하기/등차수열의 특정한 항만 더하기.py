def solution(a, d, included):
    answer = [a+d*i for i in range(len(included))]
    return sum([j* i for j,i in zip(answer,included)])
 
    