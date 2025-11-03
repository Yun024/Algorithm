import sys

input = sys.stdin.readline

strings = input().strip()
res = strings[0] 
cnt = 0

for s in strings:
    if s != res:
        break
    cnt += 1
    
print(cnt)