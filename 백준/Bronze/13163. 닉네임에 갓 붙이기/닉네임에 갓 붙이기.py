import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = input().split()
    strings[0] = "god"
    print(''.join(strings))