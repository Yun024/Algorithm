import sys
input = sys.stdin.readline

def matrix_multiple(matrix_a,matrix_b,n):

    ans = [[0]*n for _ in range(n)]
    
    for x in range(n):   
        for y in range(n):
            num = 0
            for z in range(n):
                num += matrix_a[x][z] * matrix_b[z][y]
            ans[x][y] = num % 1000
    return ans

def daq(matrix,b):

    if b == 1:
        return [[j%1000 for j in i] for i in matrix]
    
    half = daq(matrix,b//2)
    squared = matrix_multiple(half,half,n)

    return matrix_multiple(matrix,squared,n) if b%2 == 1 else squared

n,b = map(int,input().split())
matrix = [list(map(int,input().split())) for _ in range(n)]

for i in daq(matrix,b):
    print(*i)