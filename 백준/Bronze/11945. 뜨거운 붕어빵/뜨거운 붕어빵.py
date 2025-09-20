import sys
input = sys.stdin.readline

n,m = map(int,input().split())
for _ in range(n):
    s = input().strip()
    print(s[::-1])