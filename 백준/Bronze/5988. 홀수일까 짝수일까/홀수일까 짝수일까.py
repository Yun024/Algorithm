import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = int(input().strip())
    if strings%2:
        print("odd")
    else:
        print("even")