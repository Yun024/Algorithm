import sys
s,m = map(int,sys.stdin.readline().split())

mask = (1<<10)-1
if s <= mask:
    print("No thanks")
else:
    if (s-mask)&m == s-mask:
        print("Thanks")
    else:
        print("Impossible")