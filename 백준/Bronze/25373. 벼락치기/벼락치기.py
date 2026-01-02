import sys

n = int(sys.stdin.readline().strip())

num = 0
if n <= 28:
    while n > 0:
        num += 1
        n -= num
    print(num)

else:
    temp = [i for i in range(max(0,n//7-3),n//7+4)]
    if sum(temp) < n:
        print(temp[-1]+1)
    else:
        print(temp[-1])