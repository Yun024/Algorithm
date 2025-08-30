import sys,re

input()
strings = sys.stdin.readline().strip()
m = sum(list(map(int,re.findall('[0-9]+',strings))))
print(m)
