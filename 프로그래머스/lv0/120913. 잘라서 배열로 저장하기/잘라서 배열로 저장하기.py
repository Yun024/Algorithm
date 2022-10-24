def solution(my_str, n):
    answer = []
    if len(my_str)/n == int(len(my_str)/n):
        for i in range(len(my_str)//n):
            answer.append(my_str[i*n:(1+i)*n])
    else : 
        for i in range(len(my_str)//n):
            answer.append(my_str[i*n:(1+i)*n])
        answer.append(my_str[(i+1)*n:len(my_str)])
    return answer