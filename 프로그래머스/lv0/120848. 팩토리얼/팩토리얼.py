def solution(n):
    i,j = 1,1
    while j <= n:
        i +=1
        j = j * i
    return i-1