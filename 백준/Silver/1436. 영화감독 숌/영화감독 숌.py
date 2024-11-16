answer = []
num = 666
while 1:
    if '666' in str(num):
        answer.append(num)
    num +=1 
    if len(answer) == 10000:
        break
        
print(answer[int(input())-1])