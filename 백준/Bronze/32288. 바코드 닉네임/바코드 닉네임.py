import sys
input = sys.stdin.readline

n = input().strip()
strings = input().strip()

ans = ""
for s in strings:
    if s == "l":
        ans += "L"
    else:
        ans += "i"
print(ans)