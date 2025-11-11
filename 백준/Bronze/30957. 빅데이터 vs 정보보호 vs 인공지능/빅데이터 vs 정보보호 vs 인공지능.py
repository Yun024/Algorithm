import sys
input = sys.stdin.readline

n = int(input().strip())
strings = input().strip()

B,S,A = 0,0,0
for s in strings:
    if s == "S":
        S += 1
    elif s == "B":
        B += 1
    else:
        A += 1
    
max_cnt = max(B,S,A)
ans = ""
if B == max_cnt:
    ans += "B"
if S == max_cnt:
    ans += "S"
if A == max_cnt:
    ans += "A"

print("SCU" if len(ans) == 3 else ans)