import sys
c = sys.stdin.readline().strip()
if len(c) == 2:
    print(sum(map(int,c)))
elif len(c) == 4:
    print(20)
else:
    print(int(c.replace("10",""))+10)
