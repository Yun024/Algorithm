import sys,re
input = sys.stdin.readline

input()
strings = input().strip()
print(sum(map(int,re.findall('[0-9]+',strings))))