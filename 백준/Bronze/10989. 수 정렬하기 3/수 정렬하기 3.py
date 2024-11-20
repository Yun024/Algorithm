import sys
input = sys.stdin.readline
a = int(input())
b = {i:0 for i in range(1,10001)}
for i in range(a):
    b[int(input())] += 1     
for i in b.items():
    for j in range(i[1]):
        print(i[0])
