import sys,re

sentence = sys.stdin.read().split("BULLSHIT")[:-1]

left,right = 0,len(sentence)
for words in sentence:
    temp = re.findall("[A-Za-z]+",words.lower())
    left += len(set(temp))

ans1,ans2 = left,right
while right:
    left,right = right,left%right

print(str(ans1//left),"/",str(ans2//left))