num = int(input())
answer = []
for i in range(num//2,num):
    if i + sum(map(int,list(str(i)))) == num:
        answer.append(i)
print(min(answer)) if answer else print(0)