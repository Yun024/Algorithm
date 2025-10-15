import sys
input = sys.stdin.readline

while 1:
    strings = input().strip('\n')
    if strings == "***":
        break
    else:
        print(strings[::-1])