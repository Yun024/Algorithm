import sys 
input = sys.stdin.readline
a = int(input())
b = [list(map(int,input().split())) for i in range(a)]
for i in sorted(b,key=lambda x: (x[1],x[0])):
    print(*i)