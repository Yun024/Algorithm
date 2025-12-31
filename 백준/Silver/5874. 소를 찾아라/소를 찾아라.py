import sys
strings = sys.stdin.readline().strip()

ans = 0
left_cnt = 0
for i in range(len(strings)-1):
    temp = strings[i] + strings[i+1]
    if temp == "((":
        left_cnt += 1
    elif temp == "))":
        ans += left_cnt

print(ans)