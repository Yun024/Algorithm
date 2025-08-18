import sys
from itertools import combinations
input = sys.stdin.readline
n,m = map(int,input().split())

mel_dic = {}
for _ in range(n):
    name,melody = input().split()
    mel_dic[name] = melody

cnt,ans,b = 0,-1,0
for num in range(1,n+1):
    for mel in combinations(mel_dic.keys(),num):
        temp = [0]*m
        for ml in mel:
            for i,v in enumerate(mel_dic[ml]):
                if v == 'Y':
                    temp[i] = 1
        sum_tmp = sum(temp)
        if sum_tmp > cnt:
            cnt = sum_tmp 
            ans = num
            if sum_tmp == m:
                b = 1
                break
    if b:
        break
        
print(ans)