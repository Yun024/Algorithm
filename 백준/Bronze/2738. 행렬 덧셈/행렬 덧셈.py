a,b = map(int,input().split())
am = []
for i in range(a):
    am.append(list(map(int,input().split())))
bm = []
for i in range(a):
    bm.append(list(map(int,input().split())))
cm = [[u+d for u,d in zip(j,i)] for j,i in zip(am,bm)]
for i in range(a):
    print(*cm[i])