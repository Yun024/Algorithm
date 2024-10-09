def solution(s):
    answer = []
    for i in s:
        if not(answer):
            answer.append(i)
        else:
            if i == answer[-1]:
                answer.pop()
            else:
                answer.append(i)
    return 0 if answer else 1
        
    
            
            
    
        
                
        