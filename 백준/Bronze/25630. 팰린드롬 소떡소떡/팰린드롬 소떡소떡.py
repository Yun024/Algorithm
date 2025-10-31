import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

if n%2:
    first = strings[:n//2]
    second = strings[n//2+1:]
else:
    first = strings[:n//2]
    second = strings[n//2:]

ans = 0
for f,s in zip(first,second[::-1]):
    if f != s:
        ans += 1
print(ans)


