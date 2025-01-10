import sys
input = sys.stdin.readline
input()
dic = {}
num_list = list(map(int,input().split()))
for i in num_list:
    dic[str(i)]= dic.get(str(i),0)+1
input()
print(*[dic.get(str(i),0) for i in list(map(int,input().split()))])
