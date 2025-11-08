import sys
input = sys.stdin.readline

strings = input().strip().lower()
dh = ['social','history','language','literacy']
pb = ['bigdata','public','society']

for d in dh:
    if d in strings:
        ans = 0

for p in pb:
    if p in strings:
        ans = 1

print('public bigdata' if ans else 'digital humanities')