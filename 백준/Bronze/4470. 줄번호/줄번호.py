import sys
input = sys.stdin.readline

t = int(input().strip())
for n in range(t):
    strings = input().rstrip()
    print(f'{str(1+n)}. {strings}')