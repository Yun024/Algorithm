def solution(num_list):
    for j,i in enumerate(num_list):
        if i<0 :
            return j
    return -1        
    