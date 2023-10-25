def solution(numLog):
    answer = []
    for i in range(1,len(numLog)):
        if i != len(numLog):
            answer.append(numLog[i] - numLog[i-1])
    dict = {1:'w',-1:'s',10:'d',-10:'a'}
    return ''.join([dict[i] for i in answer])
    
    
    
