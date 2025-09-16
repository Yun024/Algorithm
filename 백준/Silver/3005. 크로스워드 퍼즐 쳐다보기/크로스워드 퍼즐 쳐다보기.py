import sys
input = sys.stdin.readline

r,c = map(int,input().split())
puzzle = sys.stdin.read().strip().split("\n")
res = []
for word in puzzle:
    for s in word.split("#"):
        if len(s) >= 2:
            res.append(s)
for i in range(c):
    temp = ''.join([puzzle[j][i] for j in range(r)])
    for s in temp.split("#"):
        if len(s) >= 2:
            res.append(s)
print(sorted(res)[0])