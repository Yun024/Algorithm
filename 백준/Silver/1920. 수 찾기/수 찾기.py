import sys
input = sys.stdin.readline

n = int(input().strip())
ns = list(map(int,input().split()))
m = int(input().strip())
ms = list(map(int,input().split()))

dic = {i:1 for i in ns}
for i in ms:
    print(dic.get(i,0))