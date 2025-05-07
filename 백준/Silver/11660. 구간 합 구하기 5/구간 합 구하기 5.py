import sys

input = sys.stdin.readline
n,m = map(int,input().split())

def table_sum(n,m):

    table = [list(map(int,input().split())) for _ in range(n)]
    ts = table[:]

    for i in range(n):
        for j in range(n):
            if j != 0 :
                ts[i][j] += ts[i][j-1]

    answer = []
    for _ in range(m):
        x1,y1,x2,y2 = map(int,input().split())
        ans = 0
        for i in range(x1-1,x2):
            if y1 == 1:
                ans += ts[i][y2-1]   
            else:
                ans += ts[i][y2-1] - ts[i][y1-2]
        answer.append(ans)

    return answer

answer = table_sum(n,m)

for i in answer:
    print(i)