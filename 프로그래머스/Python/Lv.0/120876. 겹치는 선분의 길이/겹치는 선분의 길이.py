def solution(lines):
    answer = 0
    all = sum([list(range(i[0],i[1])) for i in [i for i in lines]],[])
    for i in list(set(all)):
        if all.count(i) > 1 :
            answer +=1 
    return answer
        