import sys
a= int(sys.stdin.readline())

[print(sum(map(int,sys.stdin.readline().split()))) for i in range(a)]
