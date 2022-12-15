def solution(n):
    x = 2
    answer= []
    while n/x  != 1:
        if n/x == n//x :
            n = n /x 
            answer.append(x)
        else :
            x += 1 
    answer.append(x)
    return sorted(list(set(answer)))
    