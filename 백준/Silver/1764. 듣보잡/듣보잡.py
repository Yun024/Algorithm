import sys
input = sys.stdin.readline
n,m = map(int,input().split())
dic = {input().strip():1 for _ in range(n)}
ans = sorted([c for _ in range(m) if dic.get(c:=input().strip(),0)])
print(len(ans))
for i in ans:
    print(i)