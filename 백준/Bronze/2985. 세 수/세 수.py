import sys
input = sys.stdin.readline

a,b,c = map(int,input().split())
operators = [0,1,2,3]

for operator in operators:
    if not operator:
        if a+b == c:
            print(f"{a}+{b}={c}")
        elif a == b+c:
            print(f"{a}={b}+{c}")
    elif operator == 1:
        if a-b == c:
            print(f"{a}-{b}={c}")
        elif a == b-c:
            print(f"{a}={b}-{c}")
    elif operator == 2:
        if a*b == c:
            print(f"{a}*{b}={c}")
        elif a == b*c:
            print(f"{a}={b}*{c}")
    else:
        if a/b == c:
            print(f"{a}/{b}={c}")
        elif a == b/c:
            print(f"{a}={b}/{c}")