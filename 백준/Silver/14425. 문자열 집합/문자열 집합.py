import sys
input = sys.stdin.readline
n,m = map(int,input().split())
s = set()
for i in range(n):
    s.add(input())
print(len([i for _ in range(m) if (i := input()) in s]))
