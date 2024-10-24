a = int(input())
answer = []
while a != 1:
    for i in list(range(2,a//2+1))+[a]:
        if a%i == 0:
            a //= i
            answer.append(i)
            break
    
for i in answer:
    print(i)