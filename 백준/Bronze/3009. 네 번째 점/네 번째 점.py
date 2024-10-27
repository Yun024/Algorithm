a,b = [],[]
for i in range(3):
    aa,bb = map(int,input().split())
    if aa in a:
        a.remove(aa)
    else:
        a.append(aa)
    if bb in b:
        b.remove(bb)
    else:
        b.append(bb)
print(a[0],b[0])