import sys
input = sys.stdin.readline

ans = []
for i in range(5):
    if "FBI" in input().strip():
        ans.append(i+1)

if ans:
    for i in ans:
        print(i)
else:
    print("HE GOT AWAY!")