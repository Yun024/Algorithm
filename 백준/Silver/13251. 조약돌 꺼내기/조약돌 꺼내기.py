import sys, math
input = sys.stdin.readline

m = int(input().strip())
colors = list(map(int,input().split()))
k = int(input().strip())

num = sum(colors)
down = math.prod([i for i in range(num,num-k,-1)])
up = 0
for color in colors:
    temp = 1
    for i in range(color,color-k,-1):
        temp *= i
    up += temp

print(up/down)