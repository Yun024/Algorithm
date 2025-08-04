import sys
w,h,k,t = map(int,sys.stdin.readline().split())
mod = 998244353
ans = 1
virus = sys.stdin.read().strip().split("\n")
for v in virus:
    x,y = map(int,v.split())
    left = max(1,x - t)
    right = min(w,x + t)
    high = max(1,y - t)
    low = min(h,y + t)
    
    ans = ans * (right - left + 1) % mod
    ans = ans * (low - high + 1) % mod

print(ans)