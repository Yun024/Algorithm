import sys

a,b,c = map(int,sys.stdin.readline().split())
def daq(a,b,c):

    if b == 0:
        return 1
    else:
        if b%2 == 0:
            return daq(a,b//2,c)**2 % c
        else:
            return a*daq(a,b//2,c)**2 % c
        
print(daq(a,b,c))

