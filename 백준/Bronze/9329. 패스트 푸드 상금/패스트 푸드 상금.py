import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n,m = map(int,input().split())
    K = []
    for _ in range(n):
        K.append(list(map(int,input().split())))
    stickers = list(map(int,input().split()))
    ans = 0
    for k in K:
        ans += min([stickers[i-1] for i in k[1:-1]])*k[-1]
    print(ans)
