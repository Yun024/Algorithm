import sys

ml,mr,tl,tr = sys.stdin.readline().split()
if ml == mr == "R":
    if "P" in [tl,tr]:
        print("TK")
    elif tl == tr == "S":
        print("MS")
    else:
        print("?")
elif ml == mr == "P":
    if "S" in [tl,tr]:
        print("TK")
    elif tl == tr == "R":
        print("MS")
    else:
        print("?")
elif ml == mr == "S":
    if "R" in [tl,tr]:
        print("TK")
    elif tl == tr == "P":
        print("MS")
    else:
        print("?")
elif tl == tr == "R":
    if "P" in [ml,mr]:
        print("MS")
    elif ml == mr == "S":
        print("TK")
    else:
        print("?")
elif tl == tr == "P":
    if "S" in [ml,mr]:
        print("MS")
    elif ml == mr == "R":
        print("TK")
    else:
        print("?")
elif tl == tr == "S":
    if "R" in [ml,mr]:
        print("MS")
    elif ml == mr == "P":
        print("TK")
    else:
        print("?")
else:
    print("?")