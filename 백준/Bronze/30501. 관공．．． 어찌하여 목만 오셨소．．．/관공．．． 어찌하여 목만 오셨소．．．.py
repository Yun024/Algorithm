import sys
input = sys.stdin.readline

n = int(input().strip())
for _ in range(n):
    temp = input().strip()
    if 'S' in temp:
        print(temp)
        break