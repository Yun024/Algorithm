import sys
input = sys.stdin.readline

n = int(input().strip())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ans = 0
for aa,bb in zip(a,b):
    if aa > bb:
        ans += aa-bb
print(ans)