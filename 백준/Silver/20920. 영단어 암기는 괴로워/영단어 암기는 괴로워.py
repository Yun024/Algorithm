import sys
input = sys.stdin.readline
n,c = map(int,input().split())
dic = {}
for i in range(n):
    word = input().strip()
    if len(word) >= c :
        if dic.get(word,0):
            dic[word] +=1
        else:
            dic[word] = 1
tupl = [(k,v) for k,v in dic.items()]
tupl.sort(key=lambda x: x[0])
tupl.sort(key=lambda x: len(x[0]),reverse=True)
tupl.sort(key=lambda x: x[1],reverse=True)
for j,i in tupl:
    print(j)
