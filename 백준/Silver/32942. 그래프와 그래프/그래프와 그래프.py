import sys

a,b,c = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(11)]

for x in range(1,11):
    for y in range(1,11):
        if a*x + b*y == c:
            graph[x].append(y)

for i in range(1,11):
    if not graph[i]:
        print(0)
    else:
        print(*graph[i])