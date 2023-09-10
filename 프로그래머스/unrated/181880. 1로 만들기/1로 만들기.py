def solution(num_list):
    c= 0
    for i in num_list:
        while i != 1:
            if i %2 == 0:
                i = i/2
                c +=1
            elif i %2 != 0 :
                i = (i-1)/2
                c +=1
    return c
                
        
            