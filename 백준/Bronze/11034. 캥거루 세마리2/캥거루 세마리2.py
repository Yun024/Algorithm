import sys

inpt = sys.stdin.read().strip().split("\n")
for i in inpt:
    a,b,c = map(int,i.split())
    num = 0
    while a!=b!=c:
        if b-a > c-b:
            c = a+1
        else:
            a = c-1
        num +=1
        a,b,c = sorted([a,b,c])
    print(num-1)