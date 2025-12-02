import sys
input = sys.stdin.readline

t = int(input().strip())
for _ in range(t):
    num = int(input().strip())
    res = bin(num)[2:]
    left,right = len(res), int(res[1:],2)+1
    while left:
        print(str(left) + str(right).zfill(18))
        left -= 1
        right = right//2 + right%2