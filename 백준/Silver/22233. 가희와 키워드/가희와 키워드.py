import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = set()

for _ in range(n):
    ans.add(input().strip())
    
for i in sys.stdin.read().strip().split("\n"):
    ans -= set(i.split(","))
    print(len(ans))