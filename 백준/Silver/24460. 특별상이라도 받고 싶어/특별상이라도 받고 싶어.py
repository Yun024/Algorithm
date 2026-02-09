import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def divide(r,c,n):
    if n == 2:
        temp = [
            prizes[r][c],
            prizes[r][c+1],
            prizes[r+1][c],
            prizes[r+1][c+1]
        ]
        temp.sort()
        return temp[1]

    half = n//2
    res = [
        divide(r,c,half),
        divide(r,c+half,half),
        divide(r+half,c,half),
        divide(r+half,c+half,half)
    ]
    res.sort()
    return res[1]

n = int(input().strip())
prizes = [list(map(int,input().split())) for _ in range(n)]
print(prizes[0][0] if n==1 else divide(0,0,n))