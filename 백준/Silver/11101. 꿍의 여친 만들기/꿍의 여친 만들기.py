import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    dic = {}
    status = input().strip().split(",")
    for s in status:
        a,b = s.split(":")
        dic[a] = int(b)
    
    temp  = input().strip().split("|")
    ans = min([max([dic[j] for j in i.split("&")]) for i in temp])
    print(ans)