import sys,math
r,c,w = map(int,sys.stdin.readline().split())
r,c = r-1,c-1

ans = 0
for i in range(w):
    for j in range(i+1):
        ans += math.comb(r+i,c+j)

print(ans)