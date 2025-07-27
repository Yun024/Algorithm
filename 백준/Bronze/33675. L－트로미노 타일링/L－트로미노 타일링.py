import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    num = int(input().strip())
    if num%2:
        print(0)
    else:
        print(2**(num//2))