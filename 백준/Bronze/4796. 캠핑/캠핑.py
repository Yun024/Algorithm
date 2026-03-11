import sys
input = sys.stdin.readline
cnt = 1
while 1:

    l,p,v = map(int,input().split())
    if not sum([l,p,v]):
        break
    ans = v//p*l + (l if v%p > l else v%p)
    print(f"Case {cnt}: {ans}")
    cnt += 1
