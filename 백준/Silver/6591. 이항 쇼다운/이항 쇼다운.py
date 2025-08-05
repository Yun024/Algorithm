import sys,math
input = sys.stdin.readline

while 1:
    n,k = map(int,input().split())
    if not n and not k:
        break
    print(math.comb(n,k))