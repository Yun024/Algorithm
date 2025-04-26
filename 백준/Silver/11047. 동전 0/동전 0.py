import sys

input = sys.stdin.readline
n,num = map(int,input().split())
num_list = list(map(lambda x: int(x.strip()),sys.stdin.readlines()))[::-1]

cnt, ans = 0,0

while num:
    if num // num_list[ans]:
        cnt += num // num_list[ans]
        num %= num_list[ans]
    ans +=1

print(cnt)