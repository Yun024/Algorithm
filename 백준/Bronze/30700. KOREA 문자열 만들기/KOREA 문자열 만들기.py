import sys

strings = sys.stdin.readline().strip()
ans,cnt,name = "",0,"KOREA"

for s in strings:
    if name[cnt%5] == s:
        ans += s
        cnt += 1
print(len(ans))