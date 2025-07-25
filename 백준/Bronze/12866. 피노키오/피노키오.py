import sys
input = sys.stdin.readline

n = int(input().strip())
s = input().strip()

ans = 1
for i in ['A','C','G','T']:
    ans *= s.count(i)
print(ans%1000000007)