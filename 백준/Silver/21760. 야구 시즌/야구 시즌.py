import sys,math
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    
    n,m,k,d = map(int,input().split())
    A = n*math.comb(m,2)*k
    B = math.comb(n,2)*m**2
    temp = A+B
    ans = temp * (d//temp)
    if not ans:
        print(-1)
    else:
        print(ans)