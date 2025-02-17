import sys

def cantor(s):
    if len(s) == 1:
        return s
    ln = len(s)//3
    L = s[0:ln]
    mid = ' '*ln
    R = s[2*ln:]
    return cantor(L) + mid +  cantor(R)


num_list = list(map(int,sys.stdin.read().strip().split('\n')))
for i in num_list:
    s = '-' * 3**i
    print(cantor(s))