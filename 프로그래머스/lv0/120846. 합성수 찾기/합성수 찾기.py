def solution(n):
    result,j= 0,1
    while j != n+1:
        answer = 0
        for i in range(1,j+1):
            if j % i == 0:
                answer += 1
        if answer >= 3:
            result +=1 
        j+=1
    return result