num = int(input())
answer = -1
for i in range(num//5+1)[::-1]:
    num_c = num
    num_c = num_c - (5*i)
    if num_c % 3 ==0:
        answer = num_c//3 + i 
        break
print(answer)