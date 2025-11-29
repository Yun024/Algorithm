import sys
input = sys.stdin.readline

while 1:
    strings = input().strip()
    if strings == "#":
        break
    key,sentence = strings[0], strings[1:]
    print(key,sentence.lower().count(key)) 