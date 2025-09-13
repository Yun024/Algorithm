import sys,re
input = sys.stdin.readline

t = int(input().strip())
ans = []
for _ in range(t):
    temp = []
    for i in input().split(",")[:3]:
        a,b = re.findall("[A-Za-z0-9]+",i)
        temp.append(b)
    ans.append(temp)

ans = sorted(ans,key=lambda x: [-int(x[1]),x[0]])
ans[0].append(1)
for i in range(1,len(ans)):
    if ans[i][1] == ans[i-1][1]:
        ans[i].append(ans[i-1][-1])
    else:
        ans[i].append(i+1)

for i in ans:
    if not int(i[2]):
        print(i[3],i[0],i[1])