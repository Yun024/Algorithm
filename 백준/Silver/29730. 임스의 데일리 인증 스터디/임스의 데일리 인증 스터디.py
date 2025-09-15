import sys
input = sys.stdin.readline

t = int(input().strip())
boj = []
not_boj = []
for _ in range(t):
    temp = input().strip()
    if "boj.kr" in temp:
        boj.append(temp)
    else:
        not_boj.append(temp)
boj.sort(key=lambda x: int(x.split("/")[1]))
not_boj.sort(key=lambda x: [len(x),x])
for i in not_boj+boj:
    print(i)