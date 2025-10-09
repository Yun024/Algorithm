import sys
input = sys.stdin.readline

ans = []
for _ in range(3):
    ans.append(input().strip())

if ans[1] == "*":
    print(int(ans[0])*int(ans[2]))
else:
    print(int(ans[0])+int(ans[2]))
