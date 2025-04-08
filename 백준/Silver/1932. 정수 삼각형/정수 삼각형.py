import sys

input = sys.stdin.readline
n = int(input().strip())

triangle = [list(map(int,input().split())) for i in range(n)]

for i in range(1,n):
    triangle[i-1] = [0] + triangle[i-1] + [0]
    for j in range(len(triangle[i])):
        triangle[i][j] += max(triangle[i-1][j],triangle[i-1][j+1])

print(max(triangle[-1]))