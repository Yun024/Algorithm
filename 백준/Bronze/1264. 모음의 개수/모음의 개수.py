import sys
input = sys.stdin.readline

while 1:
    strings = input().strip().lower()
    if strings == '#':
        break
    cnt = 0
    for s in strings:
        if s in ['a','e','i','o','u']:
            cnt +=1
    print(cnt)