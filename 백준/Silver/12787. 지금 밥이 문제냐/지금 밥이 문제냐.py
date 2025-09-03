import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    m,n = input().split()
    if m == '1':
        temp = int(''.join([bin(i)[2:].zfill(8) for i in map(int,n.split('.'))]),2)
        print(temp)
    else:
        temp = bin(int(n))[2:]
        temp = temp.zfill(64)
        ans = [int(temp[i:i+8],2) for i in range(0,64,8)]
        print('.'.join(map(str,ans)))
        