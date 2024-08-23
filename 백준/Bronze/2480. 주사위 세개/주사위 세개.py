a,b,c = map(int,input().split())
if a==b and b==c :
    print(10000 + a*1000)
elif a==b or b==c or a== c:
    print(1000 + sorted([a,b,c])[1]*100)
else:
    print(100 * max(a,b,c))