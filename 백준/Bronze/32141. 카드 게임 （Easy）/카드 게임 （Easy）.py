import sys
input = sys.stdin.readline

n,h = map(int,input().split())
attack = list(map(int,input().split()))
length = len(attack)
ans = 0

while h > 0 and ans < length:
    h -= attack[ans]
    ans += 1

print(ans if h < 1 else -1)