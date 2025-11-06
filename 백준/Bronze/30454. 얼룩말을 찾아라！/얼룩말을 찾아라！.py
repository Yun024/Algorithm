import sys
input = sys.stdin.readline

n,l = map(int,input().split())
ans = []
for _ in range(n):

    strings = input().strip().split("0")
    res = 0
    for s in strings:
        if s:
            res += 1
    ans.append(res)

res = sorted(ans)[-1]
print(res, ans.count(res))