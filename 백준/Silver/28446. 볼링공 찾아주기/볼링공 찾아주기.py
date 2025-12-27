import sys
input = sys.stdin.readline

t = int(input().strip())
dic = {}
for _ in range(t):
    temp = input().split()
    if len(temp) == 3:
        dic[temp[2]] = temp[1]
    else:
        print(dic[temp[1]])