import sys
input = sys.stdin.readline

n = int(input().strip())
before = set(input().split())
after = set(input().split())

print(list(before - after)[0])