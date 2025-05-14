import sys

input = sys.stdin.readline
n = int(input())
num_list = list(map(int,input().split()))

dic = {}

for j,i in zip(sorted(num_list),range(len(num_list))):
    if not dic.get(j,0):
        dic[j] = [i]
    else:
        dic[j].append(i)

print(*[dic[i].pop(0) for i in num_list])