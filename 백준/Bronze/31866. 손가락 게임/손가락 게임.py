import sys

a,b = map(int,sys.stdin.readline().split())
finger = {0:5, 2:6, 5:7}


fing_a, fing_b = finger.get(a,0), finger.get(b,0)

if abs(fing_a - fing_b) == 2:
    if fing_a > fing_b:
        print(">")
    else:
        print("<")
elif abs(fing_a - fing_b) == 1:
    if fing_a > fing_b:
        print("<")
    else:
        print(">")
else:
    if fing_a > fing_b:
        print(">")
    elif fing_a < fing_b:
        print("<")
    else:
        print("=")