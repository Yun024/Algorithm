def solution(n,a,b):
    cnt = 1
    a,b = min(a,b), max(a,b)
    while 1:
        if a%2 == 1 and a+1 == b:
            break
        cnt +=1
        [a,b] = [(i+1)//2 if i%2==1 else i//2 for i in [a,b]]
    
    return cnt
    
