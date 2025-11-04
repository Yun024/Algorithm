import sys
input = sys.stdin.readline

strings = input().strip()

cnt = 0
for n in range(1,int(strings)):
    if '50' in str(n):
        cnt += 1
    cnt += 1
print(cnt+1)