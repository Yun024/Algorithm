import sys
input = sys.stdin.readline

ans = 0
temp = "A"
strings = input().strip()

for s in strings:
    res = ord(temp) - ord(s)
    ans += min(26-abs(res),abs(res))
    temp = s
    
print(ans)