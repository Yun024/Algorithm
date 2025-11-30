import sys

l,r,x = map(int,sys.stdin.readline().split())

ans = sorted(set([i|x for i in range(l,r+1)]))
for idx,val in enumerate(ans):
    if not idx:
        if val:
            print(0)
            break
        else:
            temp = 1
    else:
        if temp != val:
            print(temp)
            break
        temp += 1
else:
    print(temp)
