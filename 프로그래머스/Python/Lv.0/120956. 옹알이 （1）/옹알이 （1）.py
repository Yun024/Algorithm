def solution(babbling):
    from itertools import permutations
    
    babbling_comb = []
    result =[]
    answer = 0
    possible = ["aya","ye","woo","ma"]
    
    for i in range(len(possible)):
        babbling_comb.append(list(permutations(possible,i+1)))
    babbling_comb=sum(babbling_comb,[])
    
    for i in babbling_comb:
        result.append(''.join(i))
    
    for i in babbling:
        if i in result:
            answer+=1
    
    return answer