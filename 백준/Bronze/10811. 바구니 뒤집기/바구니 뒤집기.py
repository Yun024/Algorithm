a,b = map(int,input().split())
c = [i for i in range(1,a+1)]
for i in range(b):
    d,e = map(int,input().split())
    c[d-1:e] = reversed(c[d-1:e])
print(' '.join(map(str,c)))



