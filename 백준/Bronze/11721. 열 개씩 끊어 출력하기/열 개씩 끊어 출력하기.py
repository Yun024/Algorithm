import sys

strings = sys.stdin.readline().strip()
length = len(strings)//10
for l in range(length+1):
    print(strings[10*l:10*(l+1)])