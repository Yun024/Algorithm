import sys,re
input = sys.stdin.readline

r,c = map(int,input().split())
res = []
strings = sys.stdin.read().strip().replace("\n","")
for i in range(r):
    temp = strings[i*c:i*c+c]
    for word in re.findall("[a-z]+",temp):
        if len(word) != 1:
            res.append(word)
for i in range(c):
    temp = ""
    for j in range(r):
        temp += strings[i+j*c]
    for word in re.findall("[a-z]+",temp):
        if len(word) != 1:
            res.append(word)
print(sorted(res)[0])        