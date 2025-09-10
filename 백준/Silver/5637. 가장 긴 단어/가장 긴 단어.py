import sys,re

inpt = sys.stdin.read().strip().replace("\n"," ")
ans = re.findall("[a-zA-Z-]+",inpt)

length = len(ans[0])
word = ans[0]

for a in ans:
    if length < len(a):
        length = len(a)
        word = a
print(word.lower())
        
