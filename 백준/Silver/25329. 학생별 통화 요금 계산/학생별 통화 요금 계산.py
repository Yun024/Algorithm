import sys
input = sys.stdin.readline

t = int(input().strip())
dic = {}
for _ in range(t):
    time,name = input().split()
    h,m = time.split(":")
    total = int(h)*60 + int(m)
    if not dic.get(name,0):
        dic[name] = total
    else:
        dic[name] += total

ans = []
for idx,val in dic.items():
    if not val//100:
        ans.append((idx,10))
        continue
    temp = val - 100
    if not temp%50:
        ans.append((idx,temp//50 * 3 + 10))
    else:
        ans.append((idx,(temp//50+1) * 3 + 10))

for i in sorted(ans,key=lambda x: [-x[1],x[0]]):
    print(*i)    