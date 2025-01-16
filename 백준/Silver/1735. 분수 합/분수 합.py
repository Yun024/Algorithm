import sys
input = sys.stdin.readline
a,b = map(int,input().split())
c,d = map(int,input().split())

j,i = max(b,d), min(b,d)
m = j*i
while i != 0:
    j,i = i, j%i
ans = m//j

n,m = a * ans//b + c * ans//d, ans
o,p = max(n,m), min(n,m)
while p !=0:
    o,p = p, o%p
print(*[n//o , m//o])