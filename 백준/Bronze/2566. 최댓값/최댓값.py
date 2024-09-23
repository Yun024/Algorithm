a = []
for i in range(9):
    a.append(list(map(int,input().split())))
mx = max([max(i) for i in a])
print(mx)
for j,i in enumerate(a):
    for u,k in enumerate(i):
        if k == mx:
            print(j+1,u+1)