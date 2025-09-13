import sys,re

strings = sys.stdin.readline().strip()
ans = strings.split("x")

if 'x' not in strings:
    print(0)
elif not ans[0]:
    print(1)
elif ans[0] == "-":
    print(-1)
else:
    print(int(ans[0]))

