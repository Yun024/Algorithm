def solution(polynomial):
    x = []
    integer = []
    for i in polynomial.split("+"):
        if "x" in [j for j in i]:
            x.append(i.strip())
        else :
            integer.append(i.strip())
    x = sum([1 if len(i)==1 else int(i.split("x")[0]) for i in x]) 
    num = sum([int(i) for i in integer])
    
    if x == 0:
        if num ==0:
            return ""
        else:
            return str(num)
    elif x==1:
        if num==0:
            return "x"
        else:
            return "x + "+ str(num)   
    else :
        if num==0:
            return str(x)+"x"
        else:
            return str(x)+"x + "+ str(num)
            
    