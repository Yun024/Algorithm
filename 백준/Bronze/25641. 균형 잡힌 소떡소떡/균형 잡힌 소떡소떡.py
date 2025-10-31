import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

s_cnt,t_cnt = strings.count("s"),strings.count("t")
cnt = 0
while s_cnt != t_cnt:
    if strings[cnt] == 's':
        s_cnt -= 1
    else:
        t_cnt -= 1
    cnt += 1

print(strings[cnt:])

    