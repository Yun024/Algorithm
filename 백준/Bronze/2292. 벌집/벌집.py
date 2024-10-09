num = int(input())
answer = 1
num -= 1
while num > 0 :
    num -= 6  * answer
    answer += 1
print(answer)    