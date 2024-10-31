answer = [int(input()) for i in range(3)]
if sum(answer) != 180 :
    print('Error')
elif answer[0] != answer[1] and answer[1] != answer[2] and answer[0] != answer[2]:
    print('Scalene')
elif answer[0] == answer[1] and answer[1] == answer[2]:
    print('Equilateral')
else:
    print('Isosceles')