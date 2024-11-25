import sys
input = sys.stdin.readline
a = int(input())
b = [input().split()+[i] for i in range(a)]
c = sorted(b,key=lambda x: (int(x[0]),x[2]))
for i in c:
    print(*i[:2])