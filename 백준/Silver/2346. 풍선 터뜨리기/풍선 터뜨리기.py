input()
a = list(map(int,input().split()))
c = [(j+1,i) for j,i in enumerate(a)]
cnt = 0
ans = []
while 1:
    d = c.pop(cnt)
    ans.append(d[0])
    if not c:
        break
    if d[1] > 0:
        cnt = (cnt + d[1] - 1)%len(c)
    else:
        cnt = (cnt + d[1] ) % len(c)

print(*ans)
