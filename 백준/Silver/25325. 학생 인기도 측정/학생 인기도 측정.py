import sys
input = sys.stdin.readline

n = int(input().strip())
ans = {i:0 for i in input().split()}
for _ in range(n):
    for temp in input().split():
        ans[temp] += 1

for idx,val in sorted(ans.items(),key=lambda x: [-x[1],x[0]]):
    print(idx,val)    