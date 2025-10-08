import sys

strings = sys.stdin.readline().split("-")
print(''.join([s[0] for s in strings]))