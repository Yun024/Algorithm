import sys
input = sys.stdin.readline

s = input().strip()
dic = {'c':26, 'd':10}
ans = 1
for i,v in enumerate(s):
    if not i:
        ans *= dic[v]
        before = v
    else:
        if v == before:
            ans *= dic[v]-1
            
        else:
            ans *= dic[v]
        before = v   
print(ans)