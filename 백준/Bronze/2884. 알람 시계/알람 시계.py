a,b = map(int,input().split())
if b < 45 :
    b = b+60 -45 
    if a ==0 :
        a = 23
    else:
        a = a-1
    print(a,b)
else:
    print(a,b-45)