import sys

strings = sys.stdin.readline().strip()
ans = ""
for i in range(1,int(strings)+1):
    ans += str(i)

print(ans.index(strings)+1)