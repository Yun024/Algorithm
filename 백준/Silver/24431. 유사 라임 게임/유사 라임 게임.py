import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    n,l,f = map(int,input().split())
    dic = {}
    for i in input().split():
        temp = i[-f:]
        if not dic.get(temp,0):
            dic[temp] = 1
        else:
            dic[temp] += 1
    ans = [i//2 for i in dic.values()]
    print(sum(ans))