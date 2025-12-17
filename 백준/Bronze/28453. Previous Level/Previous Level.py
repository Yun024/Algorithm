import sys
input = sys.stdin.readline

n = int(input().strip())
nums = list(map(int,input().split()))
print(*[1 if n == 300 else 2 if n >= 275 else 3 if n >= 250 else 4 for n in nums])