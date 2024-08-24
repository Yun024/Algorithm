a,b = map(int,input().split())
ans = ['0' for i in range(a)]
for i in range(b):
    d,e,f = map(int,input().split())
    ans[d-1:e] = [str(f) for i in range(e-d+1)]
print(' '.join(ans))



