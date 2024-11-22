a = int(input())
b = [list(map(int,input().split())) for i in range(a)]
for i in sorted(b,key=lambda x: (x[0],x[1])):
    print(*i)