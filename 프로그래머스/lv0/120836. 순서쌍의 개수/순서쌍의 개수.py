def solution(n):
    answer = list()
    i = n
    while i > 0 :
        if n / i == int(n/i) : 
            zz =(i,n/i)
            answer.append(zz)
        i -=1
    return len(answer)