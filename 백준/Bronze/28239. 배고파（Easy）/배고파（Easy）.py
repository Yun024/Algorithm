import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    m = int(input().strip())
    res = reversed(bin(m)[2:])
    ans = [k for k,v in enumerate(res) if v == '1']
    if len(ans) == 1:
        print(ans[0]-1,ans[0]-1)
    else:
        print(*ans)