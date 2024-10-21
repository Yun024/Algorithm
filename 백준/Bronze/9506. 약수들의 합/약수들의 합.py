while 1:
    a= int(input())
    if a == -1:
        break
    else:
        b = []
        for i in range(1,a//2+1):
            if a%i==0:
                b.append(i)
        if sum(b) == a:
            print(str(a) + " = "+' + '.join([str(i) for i in b]))
        else:
            print(str(a) + ' is NOT perfect.')