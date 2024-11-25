int(input())
b = list(map(int,input().split()))
dic = {}
for i,v in enumerate(sorted(set(b))):
    dic[v]=i
print(*[dic[i] for i in b])