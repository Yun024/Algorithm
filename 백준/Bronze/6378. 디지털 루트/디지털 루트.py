import sys
input = sys.stdin.readline

while 1:
    strings = input().strip()
    if strings == '0':
        break
    else:
        while len(strings) > 1:
            strings = str(sum([int(s) for s in strings]))
        print(strings)