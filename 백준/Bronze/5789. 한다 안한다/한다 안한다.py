import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = input().strip()
    length = len(strings)//2
    if strings[length-1] == strings[length]:
        print("Do-it")
    else:
        print("Do-it-Not")