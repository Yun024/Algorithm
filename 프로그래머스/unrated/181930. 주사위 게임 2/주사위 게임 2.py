def solution(a, b, c):
    d= 0
    if a==b :
        d+=1 
    if a==c:
        d+=1
    if b==c:
        d+=1
        
    if d ==0 :
        return a+b+c
    elif d==1:
        return (a+b+c) * (a**2 + b**2 + c**2)
    elif d>1:
        return (a+b+c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)