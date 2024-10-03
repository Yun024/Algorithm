a,b = map(int,input().split())
answer = ''
while a != 0 :
    if a%b > 9:
        answer += chr(65 + (a%b - 10))
    else:
        answer += str(a%b)
    a = a//b
print(answer[::-1])