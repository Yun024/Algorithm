num = int(input())
answer = 4
for i in range(num):
    answer = answer * 4 - 2**(i+2) - 3
print(answer)  