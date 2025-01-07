import sys
input = sys.stdin.readline
n = int(input())
s = set()
for i in range(n):
    a,b = input().split()
    s.add(a) if b=='enter' else s.discard(a)
for i in sorted(s,reverse=True):
    print(i)