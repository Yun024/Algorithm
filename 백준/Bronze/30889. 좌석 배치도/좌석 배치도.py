import sys
input = sys.stdin.readline

n = int(input().strip())
ans  = [['.']*20 for _ in range(10)]
for _ in range(n):
    strings = input().strip()
    ans[(ord(strings[0])-65)][int(strings[1:])-1] = 'o'
for a in ans:
    print(''.join(a))