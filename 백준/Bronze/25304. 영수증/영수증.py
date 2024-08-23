a = int(input())
b = int(input())
ans = []
for i in range(b):
    c,d = map(int,input().split())
    ans.append(c*d)
if a == sum(ans):
    print('Yes')
else:
    print('No')