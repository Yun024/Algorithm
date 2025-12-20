import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().split()
if len(set([s[0] for s in strings])) == 1:
    print(1)
else:
    print(0)