import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

print(strings[::n])