import sys

strings = sys.stdin.readline().strip()
happy,sad = ":-)",":-("
hcount,scount = strings.count(happy), strings.count(sad)
if hcount or scount:
    if not (hcount - scount):
        print("unsure")
    elif hcount - scount > 0:
        print("happy")
    else:
        print("sad")
else:
    print("none")

