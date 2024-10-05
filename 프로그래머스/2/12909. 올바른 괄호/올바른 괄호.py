def solution(s):
    a = []
    for i in s:
        if i=='(':
            a.append(i)
        else:
            if a:
                a.pop()
            else:
                return False
    return False if a else True
        
            
        
        
    
    
    