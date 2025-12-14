import sys
input = sys.stdin.readline

n = int(input().strip())
v = list(map(int,input().split()))
print(sum(v) - max(v))