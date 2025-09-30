import sys
input = sys.stdin.readline

strings = [input().strip()[0] for _ in range(3)]
if ['k','l','p'] == sorted(strings):
    print('GLOBAL')
else:
    print('PONIX')