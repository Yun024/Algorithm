import sys

strings = sys.stdin.readline().strip()

ans = 0
temp,num = strings[0],1
for s in strings:
    if temp < s:
        num += 1
    else:
        num = 1
    temp = s
    ans += num
print(ans)