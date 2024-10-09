num = int(input())
answer = 1
while 1:
    num -= answer
    if num <= 0:
        break
    answer +=1
if answer % 2 ==1:
    print(str(answer - (num + answer -1 ))  +  '/' + str(1 + (num + answer -1 )))
else:
    print(str(1 -1 + num + answer) + '/' + str(answer +1 - (num + answer)))