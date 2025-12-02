import sys
input = sys.stdin.readline

n = int(input().strip())
k = input().strip()
num = int(k,2)
cnt = 0

while num:
    num = num - (num&((~num)+1))
    cnt += 1
print(cnt)