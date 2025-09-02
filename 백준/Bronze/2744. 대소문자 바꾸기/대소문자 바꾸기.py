import sys
strings = sys.stdin.readline().strip()
print(''.join([s.lower() if s.isupper() else s.upper() for s in strings]))
