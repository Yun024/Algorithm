import sys
input = sys.stdin.readline

s = input().strip()
dic = {"c":26, "d":10}
ans = 1

for i,v in enumerate(s):
    if not i:
        before = v
        ans *= dic[v]
    else:
        if before == v:
            ans *= (dic[v] - 1)
        else:
            ans *= dic[v]
        before = v
    ans %= 1000000009
print(ans)