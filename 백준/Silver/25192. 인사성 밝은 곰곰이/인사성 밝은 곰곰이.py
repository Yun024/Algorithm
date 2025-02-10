import sys
input = sys.stdin.readline
n = int(input().strip())
cnt = 0
for i in range(n):
    word = input().strip()
    if word == "ENTER":
        try:
            cnt += len(aa)
            aa = set()
        except:
            aa = set()
    else:
        try:
            aa.add(word)
        except:
            pass
cnt += len(aa)
print(cnt)