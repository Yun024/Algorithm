def solution(n):
    num,factorial = 1,1
    while factorial <= n:
        num +=1
        factorial *= num
    return num-1