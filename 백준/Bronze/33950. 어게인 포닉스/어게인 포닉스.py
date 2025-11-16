import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    strings = input().strip().replace("PO","PHO")
    print(strings)
