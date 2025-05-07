import sys

input = sys.stdin.readline
n,m = map(int,input().split())

def table_sum(n,m):

    table = [list(map(int,input().split())) for _ in range(n)]
    ts = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if i == 0:
                ts[i][j] = ts[i][j-1] + table[i][j]
            elif j == 0:
                ts[i][j] = ts[i-1][j] + table[i][j]
            elif i == 0 and j == 0:
                ts[i][j] = table[i][j]
            else:
                ts[i][j] = ts[i-1][j] + ts[i][j-1] - ts[i-1][j-1] + table[i][j]

    answer = []
    for _ in range(m):
        x1,y1,x2,y2 = list(map(lambda x: int(x)-1, input().split()))

        ans = ts[x2][y2]
        
        if x1 > 0 and y1 > 0:
            ans += ts[x1-1][y1-1]
        if x1 > 0:
            ans -= ts[x1-1][y2]
        if y1 > 0:
            ans -= ts[x2][y1-1]

        answer.append(ans)

    return answer

answer = table_sum(n,m)

for i in answer:
    print(i)