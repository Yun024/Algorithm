def solution(num_list):
    a = 0
    b = 0
    for i in range(len(num_list)):
        if num_list[i] % 2 == 1:
            a = a +1 
        elif num_list[i] % 2 ==0:
            b = b +1 
    return [b,a]
