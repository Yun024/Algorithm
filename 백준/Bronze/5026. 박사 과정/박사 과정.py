import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    s = input().strip()
    if '=' in s:
        print('skipped')
    else:
        a,b = map(int,s.split('+'))
        print(a+b)