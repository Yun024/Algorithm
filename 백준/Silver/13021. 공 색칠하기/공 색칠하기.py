import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = [0]*n
for num in range(m):
    l,r = map(int,input().split())
    for i in range(l-1,r):
        ans[i] = num+1

temp = ans[0]
cc = set()
cc.add(temp)
if not temp:
    answer = 1
else:
    answer = 2
for i in ans:
    if i != temp:
        temp = i
        if i and i not in cc:
            answer *= 2
            cc.add(i)
print(answer)