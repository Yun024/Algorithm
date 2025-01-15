import sys
input = sys.stdin.readline
a,b = sorted(map(int,input().split()))
ans = a*b
while b !=0:
    a,b = b, a%b
print(ans//a)