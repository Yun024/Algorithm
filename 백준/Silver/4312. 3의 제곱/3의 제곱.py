import sys
input = sys.stdin.readline

while 1:
    n = int(input().strip())
    if not n:
        break
    res = bin(n-1).split("b")[1]
    ans = set()
    for i,v in enumerate(res[::-1]):
        if int(v):
            ans.add(3**i)
    if not ans:
        print("{ }")
    else:
        print("{ " + ', '.join(map(str,sorted(ans))) + " }")