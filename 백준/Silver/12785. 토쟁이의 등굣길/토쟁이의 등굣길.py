import sys,math
input = sys.stdin.readline

w,h = map(int,input().split())
x,y = map(int,input().split())
ans = math.comb(x-1+y-1,x-1) * math.comb(w-x+h-y,h-y) % 1000007
print(ans)