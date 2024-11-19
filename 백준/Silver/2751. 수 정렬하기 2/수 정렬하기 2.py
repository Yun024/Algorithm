import sys

input = sys.stdin.readline

a = int(input())
b = sorted([int(input()) for i in range(a)])

for i in b:
    print(i)
