import sys
input = sys.stdin.readline
n,p = map(int,input().split())
dic1, dic2 = {}, {}
for i in range(n):
    pokemon = input().strip()
    dic1[pokemon] = i+1
    dic2[str(i+1)] = pokemon

for _ in range(p):
    prob = input().strip()
    if prob.isalpha():
        print(dic1[prob])
    else:
        print(dic2[prob])
