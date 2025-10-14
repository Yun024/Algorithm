import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = input().strip()
    print(strings[0].upper() + strings[1:])