import sys

n,m = map(int,sys.stdin.readline().split())
nm = [list(map(lambda x: int(x),sys.stdin.readline().split())) for _ in range(n)]
m,k = map(int,sys.stdin.readline().split())
mk = [list(map(lambda x: int(x),sys.stdin.readline().split())) for _ in range(m)]



for i in range(n):
    ans = [0] * k
    for j in range(m):
        for u in range(k):
            ans[u] += nm[i][j] * mk[j][u]

    print(*ans)