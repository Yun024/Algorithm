import sys

strings = sys.stdin.read().strip()
strings = strings.replace("\n","")
print(sum(map(int,strings.split(","))))