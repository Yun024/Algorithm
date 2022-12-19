def combination(x):
    comb = 1
    while x != 0:
        comb =  comb * x
        x = x - 1
    return comb 

def solution(balls, share):
    return combination(balls)/ (combination(balls-share)* combination(share))