import sys
input = sys.stdin.readline

n = int(input().strip())

for _ in range(n):
    res = 2015
    strings = input().strip()
    for s in set(strings):
        res -= ord(s)
    print(res)