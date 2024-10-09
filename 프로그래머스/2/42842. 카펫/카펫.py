def solution(brown, yellow):
    for i in range(1,yellow+2):
        if yellow%i == 0:
            a,b = i,yellow//i
        if a*2 + b*2 + 4 == brown:
            break
    
    return [max(a+2,b+2),min(a+2,b+2)]
        
    


