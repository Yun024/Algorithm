while 1:
    a,b,c = sorted(map(int,input().split()))
    if c == 0 :
        break
    if c>= a+b :
        print('Invalid')
    else:
        print(['Equilateral','Isosceles','Scalene'][len({a,b,c})-1])