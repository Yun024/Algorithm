import sys

input = sys.stdin.readline
n = int(input().strip())
ex_input = [input().strip() for _ in range(n)]

ans = sorted(ex_input,key=lambda x: [len(x),sum([int(i) for i in x if i.isdigit()]),x])

for i in ans:
    print(i)