import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
if n == 1 or m == 1:
    print(0)
else:
    print((n-1)*2*(m-1))