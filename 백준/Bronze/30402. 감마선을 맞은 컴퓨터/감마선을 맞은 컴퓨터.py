import sys

strings = sys.stdin.read().strip()
if 'w' in strings:
    print('chunbae')
elif 'b' in strings:
    print('nabi')
else:
    print('yeongcheol')