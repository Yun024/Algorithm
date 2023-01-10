def solution(a, b):
    for i in range(2,min(a,b)+1):
        while a%i==0 and b%i==0:
            a = a//i; b=b//i
    while b%2 == 0:
        b = b//2
    while b%5 == 0:
        b = b/5
    return 1 if b==1 else 2
        
        
        

