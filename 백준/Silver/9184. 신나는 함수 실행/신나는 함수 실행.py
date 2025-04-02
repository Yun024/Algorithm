def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return 2 ** 20

    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    elif a == b == c:
        return 2 ** a
    else:
        dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)    
    return dp[a][b][c]

import sys
input = sys.stdin.readline

dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
while 1:
    a,b,c = map(int,input().split())
    if -1 == a == b == c:
        break
    else:
        print(f"w({a}, {b}, {c}) = {w(a,b,c)}")